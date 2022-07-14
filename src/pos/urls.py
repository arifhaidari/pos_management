from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required

# from .views import PosHome
from .views import *

app_name = "pos"

urlpatterns = [
    path('', login_required(DashboardHome.as_view(), login_url="accounts:login"), name="pos_home"),
    path('chart/data/', get_data, name="dummy_data"),
    # path('dummy/data/', ChartData.as_view(), name="chart_data"), 
    path('product/enabled/', login_required(EnabledProductList.as_view(), login_url="accounts:login"), name="enabled"),
    path('product/disabled/', login_required(DisabledProductList.as_view(), login_url="accounts:login"), name="disabled"),
    path('product/<int:product_pk>/', login_required(ProductDetail.as_view(), login_url="accounts:login"), name="product_detail"),
    path('order/list/', login_required(OrderList.as_view(), login_url="accounts:login"), name="order"),
    path('order/<int:pos_order_pk>/', login_required(OrderDetail.as_view(), login_url="accounts:login"), name="order_detail"),
    path('invoice/list/', login_required(InvoiceList.as_view(), login_url="accounts:login"), name="invoice"),
    path('invoice/<int:invoice_pk>/', login_required(InvoiceDetail.as_view(), login_url="accounts:url"), name="invoice_detail"),
    path('expense/daily/', login_required(DailyExpenseList.as_view(), login_url="accounts:login"), name="daily"),
    path('expense/monthly/', login_required(MonthlyExpenseList.as_view(), login_url="accounts:login"), name="monthly"),
    path('session/all/', login_required(SessionList.as_view(), login_url="accounts:login"), name="session"),
    path('session/current/', login_required(CurrentSession.as_view(), login_url="accounts:login"), name="current_session"),
    path('session/<int:session_pk>/', login_required(SessionDetail.as_view(), login_url="accounts:login"), name="session_detail"),
    path('return/monthly/', login_required(MonthlyReturn.as_view(), login_url="accounts:login"), name="monthly_return"),
    path('return/annual/', login_required(AnnualReturn.as_view(), login_url="accounts:login"), name="annual_return"),
    path('return/<int:pos_order_pk>/', login_required(ReturnDetail.as_view(), login_url="accounts:login"), name="return_detail"),
    path('more/note/', login_required(NotificationList.as_view(), login_url="accounts:login"), name="notification"),
    path('more/category/', login_required(CategoryList.as_view(), login_url="accounts:login"), name="category"),
    path('more/variant/', login_required(VariantList.as_view(), login_url="accounts:login"), name="variant"),
    path('client/profile/', login_required(ClientProfile.as_view(), login_url="accounts:login"), name="client_profile"),
    path('log/list/', login_required(LogList.as_view(), login_url="accounts:login"), name="log_list"),
    path('log/edited/<int:log_pk>/', login_required(EditedProductDetail.as_view(), login_url="accounts:login"), name="edited_product_detail"),
    path('log/deleted/<int:log_pk>/', login_required(DeletedProductDetail.as_view(), login_url="accounts:login"), name="deleted_product_detail"),
]
