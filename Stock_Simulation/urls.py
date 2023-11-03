from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('stock_trading_simulation.urls')),
    path('stock_detail/',include('stock_detail.urls')),
    path('accounts/',include('accounts.urls'), )
]
