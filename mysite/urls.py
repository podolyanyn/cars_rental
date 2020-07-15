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
#import admin_reports

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('cars_rental/', include('cars_rental.urls')),
    path('admin/', admin.site.urls),
    #path('report_builder/', include('report_builder.urls')),
    #path(r'^report_builder/', include('report_builder.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
    #url(r'^admin/', include(admin_reports.site.urls)),
]
