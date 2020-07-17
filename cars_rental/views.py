from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from slick_reporting.views import SampleReportView  # slick_reporting
from .models import ClientContract							# slick_reporting

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