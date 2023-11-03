from django.db import models
from django.contrib.auth.models import User
class StockInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    ticker_symbol  = models.CharField(blank=True,null=True,max_length=8)
    company_name = models.CharField(blank=True,null=True,max_length=15)
    acquisition_stock_price = models.FloatField(blank=True,null=True)
    number_of_shares_purchased = models.IntegerField(blank=True,null=True)
    simulation_stock_price = models.FloatField(blank=True,null=True)
    market_capitalization_at_time_of_purchase = models.FloatField(blank=True, null=True)
    simulation_stock_profit_and_loss = models.FloatField(blank=True, null=True)
    stock_price_down_5per = models.FloatField(blank=True, null=True)
    acquisition_stock_price_fall_5per = models.FloatField(blank=True, null=True)
    acquisition_stock_price_fall_5per_profit_and_loss = models.FloatField(blank=True, null=True)
    stock_price_down_10per = models.FloatField(blank=True, null=True)
    acquisition_stock_price_fall_10per = models.FloatField(blank=True, null=True)
    acquisition_stock_price_fall_10per_profit_and_loss = models.FloatField(blank=True, null=True)
    stock_price_down_30per = models.FloatField(blank=True, null=True)
    acquisition_stock_price_fall_30per = models.FloatField(blank=True, null=True)
    acquisition_stock_price_fall_30per_profit_and_loss = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.ticker_symbol}"
    
