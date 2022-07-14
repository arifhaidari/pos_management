from django.conf.urls import url, include, re_path
from django.urls import path, include
from django.contrib import admin


from .views import UserDetailAPIView
# from .views import UserDetailAPIView, UserCategoryAPIView


app_name = "accounts"


urlpatterns = [
    # re_path(r'^(?P<phone>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
    path('<phone>/', UserDetailAPIView.as_view(), name='detail'),
    # path('<phone>/list/', UserCategoryAPIView.as_view(), name='category_list'),
]



#
    # path('update/<int:id>/', UpdateBackup.as_view(), name="update"),



