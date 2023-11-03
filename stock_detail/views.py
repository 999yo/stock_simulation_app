from django.shortcuts import render, get_object_or_404
from django.views import View
from stock_trading_simulation.models import StockInformation
from django.shortcuts import redirect
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

class StockDetailView(View):
    template_name = 'stock_detail.html/stock_data_detail.html'

    def get(self, request, pk, period="1d"):
        stock_data = get_object_or_404(StockInformation, pk=pk)
        ticker_symbol = stock_data.ticker_symbol
        acquisition_stock_price = stock_data.acquisition_stock_price
        my_share = share.Share(ticker_symbol + '.T')
        symbol_data = None
        try:
            symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                          1,
                                          share.FREQUENCY_TYPE_DAY,
                                          1)
        except YahooFinanceError as e:
            print(e.message)
        current_stock_price = symbol_data['close'][0]
  


        if current_stock_price is not None:
            number_of_shares_purchased = stock_data.number_of_shares_purchased
            market_capitalization_at_time_stock_of_purchase = stock_data.market_capitalization_at_time_of_purchase
            current_profit_and_loss = current_stock_price * number_of_shares_purchased - market_capitalization_at_time_stock_of_purchase
        else:
            current_profit_and_loss = None

        context = {
            'stock_data': stock_data,
            'ticker_symbol': ticker_symbol,
            'acquisition_stock_price': acquisition_stock_price,
            'current_stock_price': current_stock_price,
            'selected_period': period,
            'current_profit_and_loss': current_profit_and_loss,
        }

        return render(request, self.template_name, context)


    
class DelateSaveDataView(View):
    def get(self, request, pk):
        try:
            stock_data = StockInformation.objects.get(pk=pk)
            stock_data.delete()
        except StockInformation.DoesNotExist:
            pass
        return redirect('stock_data_list')