from django.urls import path, re_path
# from .views import blog_home
from .views import PricingView

app_name = "pricing"

urlpatterns = [
    # path('', blog_home, name='blog_home'),
    path('', PricingView.as_view(), name='pricing_home'),
]



