from django import forms
from .models import StockInformation
import re

class CalcForm(forms.ModelForm):
    class Meta:
        model = StockInformation
        exclude=["user","market_capitalization_at_time_of_purchase",
                "simulation_stock_profit_and_loss","simulation_stock_profit_and_loss","stock_price_down_5per",
                "acquisition_stock_price_fall_5per","acquisition_stock_price_fall_5per_profit_and_loss",
                "stock_price_down_10per","acquisition_stock_price_fall_10per","acquisition_stock_price_fall_10per_profit_and_loss",
                "stock_price_down_30per","acquisition_stock_price_fall_30per","acquisition_stock_price_fall_30per_profit_and_loss"]
        labels = {
            "ticker_symbol":"証券コード",
            "company_name" :"企業名",
            "acquisition_stock_price":"平均取得単価",
            "number_of_shares_purchased":"購入株数",
            "simulation_stock_price":"シミュレーション株価",
            "date":"株を購入した日付",
        }

        widgets = {
            'date': forms.NumberInput(attrs={
                "type": "date"
            })
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)
    
    
    def clean_ticker_symbol(self):
        ticker_symbol = self.cleaned_data.get('ticker_symbol')
        if not ticker_symbol:
            raise forms.ValidationError("証券コードを入力してください。")

        
        if not re.match(r'^\d{4}$', ticker_symbol):
            raise forms.ValidationError("証券コードは4桁の数字を入力してください。")        
        return ticker_symbol
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance