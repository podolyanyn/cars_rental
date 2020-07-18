from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from slick_reporting.views import SampleReportView  # slick_reporting
from .models import ClientContract							# slick_reporting

import csv
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Привіт. Це про аренду авто :) ")
	
	
class TotalProductSales(SampleReportView): # slick_reporting
    # The model where you have the data
    report_model = ClientContract

    # the main date field used for the model.
    date_field = 'date' # or 'order__date_placed'
    # this support traversing, like so
    # date_field = 'order__date_placed'

    # A foreign key to group calculation on
    #group_by = 'product'

    # The columns you want to display
    columns = ['date', 'number']

    # Charts
    charts_settings = [
     {
        'type': 'bar',
        'data_source': 'number',
        'title_source': 'title',
     },
    ]
	
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response