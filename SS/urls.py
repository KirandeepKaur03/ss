"""SS URL Configuration

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
"""
from django.contrib import admin
from django.urls import path
from SS_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home'),
    path('about_us/',views.about_us,name='about_us'),
    path('power/',views.power,name='power'),
    path('voltage/',views.voltage,name='voltage'),
    path('solar',views.solar,name='solar'),
    path('evehicle/',views.evehicle,name='evehicle'),
    path('shop/',views.shop,name='shop'),
    path('sel_voltage/',views.sel_voltage,name='sel_voltage'),
    path('sel_power/',views.sel_power,name='sel_power'),
    path('sel_solar/',views.sel_solar,name='sel_solar'),
    path('sel_evehicle/',views.sel_evehicle,name='sel_evehicle'),
    path('bl_1/',views.bl_1,name='bl_1'),
    path('bl_2/',views.bl_2,name='bl_2'),
    path('bl_3/',views.bl_3,name='bl_3'),
    path('bl_4/',views.bl_4,name='bl_4'),
    path('bl_5/',views.bl_5,name='bl_5'),
    path('bl_6/',views.bl_6,name='bl_6'),
    path('add_queries/',views.add_queries,name='add_queries'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_login1/', views.admin_login1, name='admin_login1'),
    path('admin_login1/queries/', views.queries, name='queries'),
    path('admin_login1/queries/delete/<int:id>/', views.query_delete, name='query_delete'),
    path('add_admin/', views.add_admin, name='add_admin'),

]
