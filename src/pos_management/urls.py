"""pos_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
    url(r'^api/auth/', include('accounts.api.urls', namespace='api-auth')),
    url(r'^api/user/', include('accounts.api.user.urls', namespace='api-user')),
    url(r'^api/status/', include('status.api.urls', namespace='api-status')),
"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import home_page, feature_page, ContactView, change_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('lang/<str:code>/', change_language, name='change_language'),
    path('feature/', feature_page, name='feature'),
    path('contact/', ContactView.as_view(), name='contact_us'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('blog/', include("blog.urls", namespace='blog')),
    path('pricing/', include("pricing.urls", namespace='pricing')),
    path('accounts/', include("accounts.urls", namespace='accounts')),
    path('pos/', include("pos.urls", namespace='pos')),
    path('dashboard/', include("dashboard.urls", namespace='dashboard')),
    
    # API endpoints
    path('api/', include("rest_api.urls", namespace="rest_api")),
    path('api/auth/', include("accounts.api.urls", namespace="api_auth")),
    path('api/user/', include("accounts.api.user.urls", namespace="api_user")),
]

if settings.DEBUG:
        urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
