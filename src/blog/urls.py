from django.urls import path, re_path
# from .views import blog_home
from .views import BlogView

app_name = "blog"

urlpatterns = [
    # path('', blog_home, name='blog_home'),
    path('', BlogView.as_view(), name='blog_home'),
]

