from django.urls import path
from .views import StockDetailView,DelateSaveDataView

urlpatterns = [
    path('stock_chart_view/<int:pk>/', StockDetailView.as_view(), name='stock_detail_view'),
    path('delete_saved_data/<int:pk>/', DelateSaveDataView.as_view(), name='delete_saved_data'),

]