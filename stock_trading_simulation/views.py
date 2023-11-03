from django.views.generic.edit import FormView
from .forms import CalcForm
from .models import StockInformation
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import sys

class CalcFormView(FormView):
    template_name = "stock_trading_simulation_HTML/home.html"
    form_class = CalcForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        ticker_symbol = form.cleaned_data['ticker_symbol']
        company_name = form.cleaned_data['company_name']
        acquisition_stock_price = form.cleaned_data['acquisition_stock_price']
        number_of_shares_purchased = form.cleaned_data['number_of_shares_purchased']
        simulation_stock_price = form.cleaned_data['simulation_stock_price']
        date = form.cleaned_data['date']
        symbol_data = None
        current_stock_price = None
        error_message = None  

        if ticker_symbol is not None:
            my_share = share.Share(ticker_symbol + '.T')
            try:
                symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY, 1, share.FREQUENCY_TYPE_DAY, 1)
                if symbol_data is not None and 'close' in symbol_data:
                    current_stock_price = symbol_data['close'][0]
                else:
                    pass
            except YahooFinanceError as e:
                print(e.message)
                
        if ticker_symbol is None or acquisition_stock_price is None or number_of_shares_purchased is None or simulation_stock_price is None or date is None:
            return render(self.request, self.template_name, {
                'form': form,
                'ticker_symbol': ticker_symbol,
                'company_name': company_name,
                'current_stock_price': current_stock_price if error_message is None else error_message,
                'simulation_stock_price': simulation_stock_price,
                'number_of_shares_purchased': number_of_shares_purchased,
                'acquisition_stock_price': acquisition_stock_price,
                'date': date,
            })

        if self.request.POST.get('calculate'):
            market_capitalization_at_time_of_purchase = acquisition_stock_price * number_of_shares_purchased
            simulation_stock_profit_and_loss = (simulation_stock_price * number_of_shares_purchased) - market_capitalization_at_time_of_purchase
            stock_price_down_5per = acquisition_stock_price * 0.95 
            acquisition_stock_price_fall_5per = market_capitalization_at_time_of_purchase * 0.95
            acquisition_stock_price_fall_5per_profit_and_loss = acquisition_stock_price_fall_5per - market_capitalization_at_time_of_purchase
            stock_price_down_10per = acquisition_stock_price * 0.90 
            acquisition_stock_price_fall_10per = market_capitalization_at_time_of_purchase * 0.90
            acquisition_stock_price_fall_10per_profit_and_loss = acquisition_stock_price_fall_10per - market_capitalization_at_time_of_purchase
            stock_price_down_30per = acquisition_stock_price * 0.7 
            acquisition_stock_price_fall_30per = market_capitalization_at_time_of_purchase * 0.7
            acquisition_stock_price_fall_30per_profit_and_loss = acquisition_stock_price_fall_30per - market_capitalization_at_time_of_purchase
        
            return render(self.request, self.template_name, {
                'form': form,
                'ticker_symbol': ticker_symbol,
                'date': date,
                'company_name': company_name,
                'current_stock_price': current_stock_price,
                'simulation_stock_price': simulation_stock_price,
                'number_of_shares_purchased': number_of_shares_purchased,
                'acquisition_stock_price': acquisition_stock_price,
                'market_capitalization_at_time_of_purchase': market_capitalization_at_time_of_purchase,
                'simulation_stock_profit_and_loss': simulation_stock_profit_and_loss,
                'stock_price_down_5per': stock_price_down_5per,
                'acquisition_stock_price_fall_5per': acquisition_stock_price_fall_5per,
                'acquisition_stock_price_fall_5per_profit_and_loss': acquisition_stock_price_fall_5per_profit_and_loss,
                'stock_price_down_10per': stock_price_down_10per,
                'acquisition_stock_price_fall_10per': acquisition_stock_price_fall_10per,
                'acquisition_stock_price_fall_10per_profit_and_loss': acquisition_stock_price_fall_10per_profit_and_loss,
                'stock_price_down_30per': stock_price_down_30per,
                'acquisition_stock_price_fall_30per': acquisition_stock_price_fall_30per,
                'acquisition_stock_price_fall_30per_profit_and_loss': acquisition_stock_price_fall_30per_profit_and_loss,
                })

        return super().form_valid(form)
        
class SaveResultsView(View):
    def post(self, request):
        if request.user.is_authenticated:
            ticker_symbol = request.POST.get('ticker_symbol')
            acquisition_stock_price = request.POST.get('acquisition_stock_price')
            number_of_shares_purchased = request.POST.get('number_of_shares_purchased')
            simulation_stock_price = request.POST.get('simulation_stock_price')
            date = request.POST.get('date')

            try:
                company_name = request.POST.get('company_name')
                market_capitalization_at_time_of_purchase = float(acquisition_stock_price) * int(number_of_shares_purchased)
                simulation_stock_profit_and_loss = (float(simulation_stock_price) * int(number_of_shares_purchased)) - market_capitalization_at_time_of_purchase
                stock_price_down_5per = float(acquisition_stock_price) * 0.95
                acquisition_stock_price_fall_5per = market_capitalization_at_time_of_purchase * 0.95
                acquisition_stock_price_fall_5per_profit_and_loss = acquisition_stock_price_fall_5per - market_capitalization_at_time_of_purchase
                stock_price_down_10per = float(acquisition_stock_price) * 0.9 
                acquisition_stock_price_fall_10per = market_capitalization_at_time_of_purchase * 0.90
                acquisition_stock_price_fall_10per_profit_and_loss = acquisition_stock_price_fall_10per - market_capitalization_at_time_of_purchase
                stock_price_down_30per = float(acquisition_stock_price) * 0.7
                acquisition_stock_price_fall_30per = market_capitalization_at_time_of_purchase * 0.70
                acquisition_stock_price_fall_30per_profit_and_loss = acquisition_stock_price_fall_30per - market_capitalization_at_time_of_purchase

                stock_info = StockInformation(
                    user=self.request.user,
                    date=date,
                    ticker_symbol=ticker_symbol,
                    company_name=company_name,
                    acquisition_stock_price=float(acquisition_stock_price),
                    number_of_shares_purchased=int(number_of_shares_purchased),
                    simulation_stock_price=float(simulation_stock_price),
                    market_capitalization_at_time_of_purchase=market_capitalization_at_time_of_purchase,
                    simulation_stock_profit_and_loss=simulation_stock_profit_and_loss,
                    stock_price_down_5per=stock_price_down_5per,
                    acquisition_stock_price_fall_5per=acquisition_stock_price_fall_5per,
                    acquisition_stock_price_fall_5per_profit_and_loss=acquisition_stock_price_fall_5per_profit_and_loss,
                    stock_price_down_10per=stock_price_down_10per,
                    acquisition_stock_price_fall_10per=acquisition_stock_price_fall_10per,
                    acquisition_stock_price_fall_10per_profit_and_loss=acquisition_stock_price_fall_10per_profit_and_loss,
                    stock_price_down_30per=stock_price_down_30per,
                    acquisition_stock_price_fall_30per=stock_price_down_30per,
                    acquisition_stock_price_fall_30per_profit_and_loss=acquisition_stock_price_fall_30per_profit_and_loss
                )
                stock_info.save()
                return JsonResponse({'message': '結果を保存しました。シミュレーションリストで保存した内容を確認できます.'})
            except ValueError:
                return JsonResponse({'message': '入力された情報が不正です。'}, status=400)
        else:
            return JsonResponse({'message': 'ログインしていないか、認証されていません。'}, status=401)


class StockDataListView(ListView):
    template_name = "stock_trading_simulation_HTML/stock_data_list.html"
    model = StockInformation
    context_object_name = "stock_data_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = StockInformation.objects.filter(user=self.request.user).order_by('acquisition_stock_price')
        for stock_data in queryset:
            symbol_data = None
            current_stock_price =None
            try:
                ticker_symbol= stock_data.ticker_symbol
                my_share = share.Share(ticker_symbol + '.T')
                symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                          1,
                                          share.FREQUENCY_TYPE_DAY,
                                          1)
                current_stock_price = symbol_data['close'][0]
                
            except YahooFinanceError as e:
                print(e.message)
                continue
                #sys.exit(1)
            if current_stock_price is not None:
                number_of_shares_purchased = stock_data.number_of_shares_purchased
                market_capitalization_at_time_stock_of_purchase = stock_data.market_capitalization_at_time_of_purchase
                stock_data.current_stock_price = current_stock_price
                current_profit_and_loss = current_stock_price * number_of_shares_purchased - market_capitalization_at_time_stock_of_purchase
                stock_data.current_profit_and_loss = current_profit_and_loss
            else:
                stock_data.current_profit_and_loss = None

        return queryset

class DelateSaveDataView(View):
    def get(self, request, pk):
        try:
            saved_data = StockInformation.objects.get(pk=pk)
            saved_data.delete()
        except StockInformation.DoesNotExist:
            pass
        return redirect('stock_data_list')
    
class AboutStockSimulation(View):
    def get(self, request):
        return render(request, 'stock_trading_simulation_HTML/about.html')
