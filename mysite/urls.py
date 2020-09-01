"""mysite URL Configuration

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
from django.urls import include, path
from django.conf.urls import url
from ra.admin.admin import ra_admin_site # django-ra-erp
from cars_rental.views import TotalProductSales # slick_reporting
import cars_rental.views


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('cars_rental/', include('cars_rental.urls')),
    path('admin/', admin.site.urls),
    url(r'^report_builder/', include('report_builder.urls')),
    #path('admin/report_builder/', include('report_builder.urls')), # цікаво себе поводить, мабуть внаслідок того, що admin накладає свої обмеження
    #path(r'^report_builder/', include('report_builder.urls')),
    #url(r'^admin/', include(admin_reports.site.urls)),
    path('erp/', ra_admin_site.urls), # django-ra-erp
    path('url-to-report', TotalProductSales.as_view()), # slick_reporting
    #url(r'^export/csv/$', cars_rental.views.export_users_csv, name='export_users_csv'),
    #url(r'^export/xls/$', cars_rental.admin.WeeklyCarReportAdminKyiv.export_users_xls, name='export_users_xls'),
    #url(r'^export/xls/$', cars_rental.views.export_users_xls, name='export_users_xls'),
    #url('myform', cars_rental.views.get_myform),
]
