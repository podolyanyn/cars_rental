from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from slick_reporting.views import SampleReportView  # slick_reporting
from .models import ClientContract							# slick_reporting

import csv
from django.contrib.auth.models import User
import xlwt


# https://djbook.ru/rel3.0/intro/tutorial03.html
def index(request):
    list = ClientContract.objects.all()
    #output = output = ', '.join([q.number for q in list])
    #return HttpResponse("Привіт. Це про аренду авто :) " + output)
	
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'list': list}
    return render(request, 'cars_rental/index.html', context)
	
# https://djbook.ru/rel3.0/intro/tutorial03.html
def detail(request, clientcontract_id):
    clientcontract = get_object_or_404(ClientContract, pk=clientcontract_id)
    return render(request, 'cars_rental/timetable_to.html', {'clientcontract': clientcontract})


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
    writer.writerow(['Нік користувача', 'Імя', 'Прізвище', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    #print ('users = ', users)
    for user in users:
        writer.writerow(user)
    
    writer.writerow(['Сума 1', 'Сума 2', 'Сума 3', 'Сума 4'])

    return response
	
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Нік', 'Імя', 'Прізвище', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response