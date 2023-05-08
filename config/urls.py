"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Market",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui("swagger")),
    path('api/v1/account/', include('user_account.urls')),
    path("api/v1/", include('product.urls')),
    path('api/v1/', include('review.urls')),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('api/v1/', include('cart.urls')),
    path('chat/', include('chat.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/v1/', include(('orders.urls', 'orders'), namespace='orders')),
    # path('celeryapp/', include('celeryapp.urls'))

]
