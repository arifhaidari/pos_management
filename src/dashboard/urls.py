from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from .views import (
    DashboardMenue, ClientList, CreateClient,
    UpdateClient, DeleteClient, ClientDetail, 
    ActivateClient,
    payment_form_organizer,
    DeletePayment,
    UpdatePayment,
    PaymentList,
)

app_name = "dashboard"

urlpatterns = [
    path('', login_required(DashboardMenue.as_view(), login_url="accounts:login"), name="dashboard_menu"),
    path('create/', login_required(CreateClient.as_view(), login_url="accounts:login"), name="create"),
    path('list/', login_required(ClientList.as_view(), login_url="accounts:login"), name="list"),
    path('detail/<int:id>/', login_required(ClientDetail.as_view(), login_url="accounts:login"), name="detail"),
    path('update/<int:id>/', login_required(UpdateClient.as_view(), login_url="accounts:login"), name="update"),
    path('delete/<int:id>/', login_required(DeleteClient.as_view(), login_url="accounts:login"), name="delete"),
    path('activate/<int:id>/', login_required(ActivateClient.as_view(), login_url="accounts:login"), name="activate_client"),
    #payment part
    path('payment/list/', login_required(PaymentList.as_view(), login_url="accounts:login"), name="payment_list"),
    path('payment/create/', payment_form_organizer, name="create_payment"),
    path('payment/delete/<int:id>/', login_required(DeletePayment.as_view(), login_url="accounts:login"), name="delete_payment"),
    path('payment/update/<int:id>/', login_required(UpdatePayment.as_view(), login_url="accounts:login"), name="update_payment"),
]
