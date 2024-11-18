"""
URL configuration for weatherapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('api/v1/<str:station>/<str:date>/',one_stat_one_date,name='one_stat_one_date'),
    path('api/v1/<str:station>/',one_stat_all_dates,name='one_stat_all_dates'),
    path('api/v1/yearly/<station>/<year>/',one_stat_one_year,name="one_stat_one_year"),
]
