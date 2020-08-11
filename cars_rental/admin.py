from django.contrib import admin
from django.db import models
from django.forms import NumberInput, TextInput, Textarea
from django.db.models import Max, Count, Sum
from datetime import date, timedelta

from django import forms
from django.template import loader
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Color, Branch, ExchangeRateKyiv, ExchangeRateLviv, ExchangeRateOdesa
# Київ
from .models import ClientKyiv, CarKyiv, ClientContractKyiv, ClientContractTimetableKyiv, ClientContractTOKyiv, ClientContractTOTodayKyiv
from .models import InvestorKyiv, InvestorContractKyiv, InvestorContractBodyTimetableKyiv, InvestorContractBodyPaymentKyiv, InvestorContractPercentagePaymentKyiv
from .models import ClientContractWeeklyCarReportKyiv 
#Львів
from .models import ClientLviv, CarLviv,  ClientContractLviv,  ClientContractTimetableLviv, ClientContractTOLviv,  ClientContractTOTodayLviv
from .models import InvestorLviv, InvestorContractLviv,  InvestorContractBodyTimetableLviv, InvestorContractBodyPaymentLviv, InvestorContractPercentagePaymentLviv 
#, YourModel 
# Одеса
from .forms import yourForm
from import_export import resources
from import_export.admin import  ExportMixin, ExportActionMixin
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin # django-ra-erp
from admin_totals.admin import ModelAdminTotals  # for Django Admin Totals
from django.db.models.functions import Coalesce  # for Django Admin Totals
from django.contrib.admin.views.main import ChangeList
from django.http import HttpResponse, Http404
import xlwt
from daterange_filter.filter import DateRangeFilter  # django-daterange-filter

#------------- Блок експериментів з віджетами
#class YourModelAdmin(admin.ModelAdmin):
#    formfield_overrides = {
#        models.FloatField: {'widget': Textarea},
        #models.FloatField: {'widget': NumberInput(attrs={'style':'width:170px', 'step':'.3'})},
#   }
#admin.site.register(YourModel, YourModelAdmin)

#class My_widjet(NumberInput):
#    template_name = 'my_widget.html'
    #def render(self, name, value, renderer, attrs=None):    
        #return """Простите Блог спот и highlight пытаются интерпритировать HTML Теги""" 
        #return """<p>{{ value|floatformat:'2' }}</p>"""
        #return format_html('<p>{{ value|floatformat:'2' }}</p>')
        #return format(value, '.2f') # працює, але одразу поля робляться тільки для читання (і роздільний знак - точка)
      #      return value # # працює (разом з template_name), але одразу поля робляться тільки для читання, (і роздільний знак - точка)
    #def format_value(value):
     #   return 1.1		
"""
class My_widjet(forms.Widget):
    template_name = 'my_widget.html'

    def get_context(self, name, value, attrs=None):
        return {'widget': {
            'name': name,
            'value': value,
        }}

    def render(self, name, value, renderer=None, attrs=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        #return mark_safe(template)
        return template
#----------- Блок експериментів з віджетами (КІНЕЦЬ)
"""
"""
#@admin.register(InvestorContract)
class InvestorContractAdmin(admin.ModelAdmin):
    #form = yourForm  # цей варіант працює, в тому розумінні що відображає поле, але не форматує фого (2 знаки після точки)
admin.site.register(InvestorContract, InvestorContractAdmin)
"""
admin.site.register(Color)
admin.site.register(Branch)


class ExchangeRateKyivAdmin(admin.ModelAdmin):
    list_display = ('date', 'sum')    
admin.site.register(ExchangeRateKyiv, ExchangeRateKyivAdmin)

class ExchangeRateLvivAdmin(admin.ModelAdmin):
    list_display = ('date', 'sum')    
admin.site.register(ExchangeRateLviv, ExchangeRateLvivAdmin)

class ExchangeRateOdesaAdmin(admin.ModelAdmin):
    list_display = ('date', 'sum')    
admin.site.register(ExchangeRateOdesa, ExchangeRateOdesaAdmin)


#@admin.register(Client)
#class ClientAdmin(ImportExportModelAdmin):
class ClientAdminKyiv(admin.ModelAdmin):
#class ClientAdmin(admin.ModelAdmin):
    # 24.04 Зміна шаблону. Правда, чомусь для всіх об'єктів цей шаблон підтягнувся, не лише для клієнта.
    # 30.05 Хоча шаблон був закритий він чомусь підтягувався для клієнта. Закешувався ? Все стало ок, лише після того, як змінив ім'я шаблону на change_form_.html
    # change_form_template = 'admin/change_form.html'     	
    list_display = ('full_name', 'phone_number', 'phone_number_2', 'phone_number_3')
    search_fields = ['full_name', 'phone_number', 'phone_number_2', 'phone_number_3']
admin.site.register(ClientKyiv, ClientAdminKyiv)

class ClientAdminLviv(ClientAdminKyiv):
    pass
admin.site.register(ClientLviv, ClientAdminLviv)


class CarAdminKyiv(admin.ModelAdmin):
    #fieldsets = [
    #   (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    #inlines = [ChoiceInline]
	# ...
    list_display = ('brand', 'model', 'production_year', 'body_number', 'license_plate', 'color', 'mileage')
    #list_filter = ['brand', 'model']
    search_fields = ['license_plate']
    #date_hierarchy = 'pub_date'
admin.site.register(CarKyiv, CarAdminKyiv)

#ra_admin_site.register(Car, CarAdmin) # django-ra-erp

class CarAdminLviv(CarAdminKyiv):
    pass
admin.site.register(CarLviv, CarAdminLviv)

#admin.site.register(CarOdesa)

class CarInline(admin.StackedInline):
    model = CarKyiv
    #extra = 1
class ClientInline(admin.StackedInline):
    model = ClientKyiv
    #extra = 1
	
	
	
class ClientContractTimetableInlineEditKyiv(admin.TabularInline):
    """ Оплата за сьогодні, менеджер може редагувати"""
    model = ClientContractTimetableKyiv
    extra = 0
    fields = ['planned_payment_date', 'planned_amount_payment_usd', 'amount_paid_usd', 'note']
    readonly_fields = ['planned_payment_date', 'planned_amount_payment_usd']
    #verbose_name = "Клієнтський контракт, графік погашення; Введення даних"
    verbose_name_plural = "Клієнтський контракт, графік погашення; Введення даних"
    classes = ['collapse']
    
    def get_queryset(self, request):
        """ Вибрати  запис з графіку погашень, якщо планова дата співпадає з сьогоднішнім днем """
        qs = super(ClientContractTimetableInlineEditKyiv, self).get_queryset(request)
        return qs.filter(planned_payment_date = date.today() )

    def has_change_permission(self, request, obj=None):
       return not request.user.groups.filter(name='ManagerKyiv').exists()

class ClientContractTimetableInlineEditLviv(ClientContractTimetableInlineEditKyiv):
    """ Оплата за сьогодні, менеджер може редагувати"""
    model = ClientContractTimetableLviv

    def get_queryset(self, request):
        """ Вибрати  запис з графіку погашень, якщо планова дата співпадає з сьогоднішнім днем """
        qs = super(ClientContractTimetableInlineEditLviv, self).get_queryset(request)
        return qs.filter(planned_payment_date = date.today() )

    def has_change_permission(self, request, obj=None):
       return not request.user.groups.filter(name='ManagerLviv').exists()
	   
class ClientContractTimetableInlineKyiv(admin.TabularInline):
    model = ClientContractTimetableKyiv
    extra = 0
    fields = ['planned_payment_date', 'planned_amount_payment_usd', 'amount_paid_usd', 'note']
    #readonly_fields = ['planned_payment_date', 'planned_amount_payment_usd', 'real_payment_date', 'amount_paid_usd', 'note']
    ordering = ['planned_payment_date']
    classes = ['collapse']
	
    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name='ManagerKyiv').exists()  
    
    def has_add_permission(self, request, obj=None):
        return not request.user.groups.filter(name='ManagerKyiv').exists()
		
    def has_change_permission(self, request, obj=None):
       return not request.user.groups.filter(name='ManagerKyiv').exists()

class ClientContractTimetableInlineLviv(ClientContractTimetableInlineKyiv):
    model = ClientContractTimetableLviv
	
    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name='ManagerLviv').exists()  
    
    def has_add_permission(self, request, obj=None):
        return not request.user.groups.filter(name='ManagerLviv').exists()
		
    def has_change_permission(self, request, obj=None):
       return not request.user.groups.filter(name='ManagerLviv').exists()

	   
class ClientContractTOTodayInlineKyiv(admin.TabularInline):
    """Дані по ТО за сьогодні, менеджер може редагувати"""
    model = ClientContractTOTodayKyiv
    extra = 0
    fields = ['date', 'sum', 'note']
    readonly_fields = ['date']
    classes = ['collapse']
    
    def get_queryset(self, request):
        """ Вибрати лише дані за поточне число """
        qs = super(ClientContractTOTodayInlineKyiv, self).get_queryset(request)
        return qs.filter(date = date.today() )	
		
class ClientContractTOTodayInlineLviv(ClientContractTOTodayInlineKyiv):
    """Дані по ТО за сьогодні, менеджер може редагувати"""
    model = ClientContractTOTodayLviv
    
    def get_queryset(self, request):
        """ Вибрати лише дані за поточне число """
        qs = super(ClientContractTOTodayInlineLviv, self).get_queryset(request)
        return qs.filter(date = date.today() )	
	
class ClientContractTOInlineKyiv(admin.TabularInline):
    """ Дані по ТО """
    model = ClientContractTOKyiv
    extra = 0
    fields = ['date', 'sum', 'note']    
    ordering = ['date']
    classes = ['collapse']
   
class ClientContractTOInlineLviv(ClientContractTOInlineKyiv):
    """ Дані по ТО """
    model = ClientContractTOLviv

   
    #readonly_fields = ['date']
	
    #def has_view_permission(self, request, obj=None):
        #""" без цього методу для менеджера невидимий весь блок ТО, якщо ще не має жодного запису """
        #return True

    #def has_add_permission(self, request, obj=None):
        #print('info =', request.user.groups.all())
        #print('self.fields =', self.fields) 
        #return True
        #return not request.user.groups.filter(name='Manager').exists()
	
    #def get_formset(self, request, obj=None):
        #formset.form.base_fields['date'].initial
        #self.fields[2].initial = 'aaaa'
        #self.initial['sum'] = 222

    #def has_delete_permission(self, request, obj=None):
        #print('info =', request.user.groups.all())
        #print('self.fields =', self.fields) 
        #return True
        #return not request.user.groups.filter(name='Manager').exists() and 
        #print ("obj = ", obj)
		
class ClientContractAdminKyiv(admin.ModelAdmin):
    #fieldsets = [
    #   (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    fields = ['number', 'number_number', 'city', 'date', 'client', 'car', 'investor_full_name', 'director_full_name', 'initial_cost_car_usd', 'commercial_course_usd_test', 'initial_cost_car_uah', 'period_days', 'frequency_payment', 'amount_payment_usd', 'amount_payment_uah', 'amount_payment_TO_uah', 'balance_TO_uah', 'loan_amount_paid_usd', 'loan_amount_to_be_paid_usd', 'status_body_usd']
    inlines = [ClientContractTOTodayInlineKyiv, ClientContractTOInlineKyiv, ClientContractTimetableInlineEditKyiv , ClientContractTimetableInlineKyiv]	 #
    #inlines = [ClientInline]
	# ...
    #fields = ['number', 'city', 'date', 'client', 'car']
    list_display = ('number', 'city', 'date', 'client', 'car', 'initial_cost_car_usd', 'loan_amount_paid_usd', 'loan_amount_to_be_paid_usd')
    #list_editable = ('city', 'date', 'client', 'initial_cost_car_usd', 'commercial_course_usd', 'initial_cost_car_uah', 'period_days')
    #list_filter = ['brand', 'model']
    #search_fields = [ 'client', 'car']
    search_fields = [ 'number', 'client__full_name',  'car__license_plate']
    readonly_fields = ['commercial_course_usd_test', 'initial_cost_car_uah', 'amount_payment_uah', 'balance_TO_uah', 'loan_amount_paid_usd', 'loan_amount_to_be_paid_usd', 'status_body_usd']
    #date_hierarchy = 'pub_date'
    def save_model(self, request, obj, form, change):
        obj.save()
        obj.timetable_calc()
        obj.to_calc()
        obj.get_commercial_course_usd_test()
        obj.calc_loan_amount_paid()
        #obj.save()
           #obj.user = request.user
        #super().save_model(request, obj, form, change)
        #self.clientcontracttimetable_set.create(planned_amount_payment_usd=222)
        #super().test()
        #super().save_model(request, obj, form, change)
		
    # початкові дані для форми нового об'єкту/редагування об'єкту. 
    def get_changeform_initial_data(self, request):
        #return {'number': '100'}
        #return obj.number_calc()
        #self.status_body = self.investorcontractbodypayment_set.all().filter(date__lte=timetable[i].payment_date).aggregate(Sum('sum'))['sum__sum']
        #sss = self.all().aggregate(Max('number_number'))
        # Розрахунок максимального номеру в поточному році. Використав скорочену форму терн. оператора. Якщо отримую None, то присвоюю 0
        max_number = ClientContractKyiv.objects.all().filter(date__year = date.today().year).aggregate(Max('number_number'))['number_number__max'] or 0
        #print ('max_number = ', max_number)		
        
        #04.06.2020  закоментовую для commercial_course_usd_test, не знаю, як дістатись до значень об'єкту obj,  тобто ClientContract (зробив через default в моделі)
        #commercial_c_u = ExchangeRateKyiv.objects.all().filter(date == self.fields['date'])
        #print ('self = ', self.fields)		
        return {'number': str(date.today().year) + '-' + str(max_number+1) + '/К', 'number_number':max_number+1} #, 'commercial_course_usd_test':commercial_c_u}
        
admin.site.register(ClientContractKyiv, ClientContractAdminKyiv)

class ClientContractAdminLviv(ClientContractAdminKyiv):
    inlines = [ClientContractTOTodayInlineLviv, ClientContractTOInlineLviv, ClientContractTimetableInlineEditLviv , ClientContractTimetableInlineLviv]
    
    def get_changeform_initial_data(self, request):
        max_number = ClientContractLviv.objects.all().filter(date__year = date.today().year).aggregate(Max('number_number'))['number_number__max'] or 0
        return {'number': str(date.today().year) + '-' + str(max_number+1) + '/Л', 'number_number':max_number+1} #, 'commercial_course_usd_test':commercial_c_u}
admin.site.register(ClientContractLviv, ClientContractAdminLviv)    




class InvestorAdminKyiv(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')
    search_fields = ['full_name', 'phone_number']
admin.site.register(InvestorKyiv, InvestorAdminKyiv)

class InvestorAdminLviv(InvestorAdminKyiv):
    pass
admin.site.register(InvestorLviv, InvestorAdminLviv)


class InvestorContractBodyTimetableInlineKyiv(admin.TabularInline):
    model = InvestorContractBodyTimetableKyiv
    extra = 0
    #can_delete = False
    fields = ['payment_date', 'payment_percentage', 'payment_usd']
    #readonly_fields = ['payment_usd']

class InvestorContractBodyTimetableInlineLviv(InvestorContractBodyTimetableInlineKyiv):
    model = InvestorContractBodyTimetableLviv


	

class InvestorContractBodyPaymentInlineKyiv(admin.TabularInline):
    model = InvestorContractBodyPaymentKyiv
    extra = 0
    #can_delete = False
    fields = ['date', 'sum']
    #readonly_fields = ['payment_usd']
	
class InvestorContractBodyPaymentInlineLviv(InvestorContractBodyPaymentInlineKyiv):
    model = InvestorContractBodyPaymentLviv

	
	
	
class InvestorContractPercentagePaymentInlineKyiv(admin.TabularInline):
    model = InvestorContractPercentagePaymentKyiv
    extra = 0
    fields = ['date', 'sum']
    #readonly_fields = ['planned_payment_date', 'planned_amount_payment_usd']
	
class InvestorContractPercentagePaymentInlineLviv(InvestorContractPercentagePaymentInlineKyiv):
    model = InvestorContractPercentagePaymentLviv

	
	
class InvestorContractAdminKyiv(admin.ModelAdmin):
    #fieldsets = [
    #   (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    fields = ('number', 'specification_number', 'city', 'date', 'investor',  'director_full_name', 'client_full_name', 'car', 'initial_cost_car_usd', 'initial_cost_car_uah', 'period_days', 'number_periods', 'status_body', 'іnterest_rate', 'last_month_percentage', 'status_percentage' )
    readonly_fields = ['number', 'specification_number']
    
    inlines = [InvestorContractBodyTimetableInlineKyiv, InvestorContractBodyPaymentInlineKyiv, InvestorContractPercentagePaymentInlineKyiv]

    list_display = ('number', 'specification_number', 'city', 'date', 'investor', 'car')
    #list_editable = ('city', 'date', 'client', 'initial_cost_car_usd', 'commercial_course_usd', 'initial_cost_car_uah', 'period_days')
    #list_filter = ['brand', 'model']
    #search_fields = [ 'client', 'car']
    search_fields = [ 'number', 'investor__full_name',  'car__license_plate']
    #date_hierarchy = 'pub_date'    

#    formfield_overrides = {
#       models.FloatField: {'widget': My_widjet},
#       #models.FloatField: {'widget':NumberInput(attrs={'style':'width:100px', 'min':'0', 'max':'1000', 'step':'.1'})}
#    }

    #def status_percentage_new(self, obj):
        #return format(obj.status_percentage, '.2f')
     #   return obj.status_percentage
    #create_time_display.short_description = '<желаемое имя>'
    
    def save_model(self, request, obj, form, change):
        # (ПЕРЕВІРИТИ ВЕСЬ РОЗРАХУНОК !!!) Розрахунок номеру контракту та номеру специфікації для даного клієнта
        # Визначаємо, чи в даного інвестора взагалі є контракти 
        contracts_set = InvestorContractKyiv.objects.all().filter(investor = obj.investor)
        print ('contracts_set = ', contracts_set )
        if not contracts_set.exists():
            obj.number = InvestorContractKyiv.objects.all().aggregate(Max('number'))['number__max'] or 0
            obj.number += 1    
            # Не враховуємо номер контракту даного об'єкту, інакше при зберіганні він його постійно збільшуватиме +1 (??? порібно подумати)
            #contract_max_number = InvestorContract.objects.all().exclude(number = obj.number).aggregate(Max('number'))['number__max'] or 0    
        else: # якщо в інвестора вже є контракт
            obj.number = contracts_set[0].number #номер контракту
        # !!! тут перевірити, оскільки при повторному зберіганні збільшується на 1
        result = InvestorContractKyiv.objects.all().filter(investor = obj.investor).aggregate(Max('specification_number'))['specification_number__max']
        obj.specification_number =  result + 1 if result else 1
        #print ('max_number = ', max_number )
        #obj.number = max_number+1
        
        #
        obj.save()
        #obj.bodytimetable_calc()
        #obj.status_body_calc() # видала система помилку при відсутності платежів по тілу: unsupported operand type(s) for -: 'NoneType' and 'float'
        obj.percentage_calc()
        if obj.control_number_periods() == False:
            self.message_user(request, "tttr")		
       #
admin.site.register(InvestorContractKyiv, InvestorContractAdminKyiv)


class InvestorContractAdminLviv(InvestorContractAdminKyiv):

    inlines = [InvestorContractBodyTimetableInlineLviv, InvestorContractBodyPaymentInlineLviv, InvestorContractPercentagePaymentInlineLviv]

    def save_model(self, request, obj, form, change):
        # (ПЕРЕВІРИТИ ВЕСЬ РОЗРАХУНОК !!!) Розрахунок номеру контракту та номеру специфікації для даного клієнта
        # Визначаємо, чи в даного інвестора взагалі є контракти 
        contracts_set = InvestorContractLviv.objects.all().filter(investor = obj.investor)
        print ('contracts_set = ', contracts_set )
        if not contracts_set.exists():
            obj.number = InvestorContractLviv.objects.all().aggregate(Max('number'))['number__max'] or 0
            obj.number += 1  
            # Не враховуємо номер контракту даного об'єкту, інакше при зберіганні він його постійно збільшуватиме +1 (??? порібно подумати)
            #contract_max_number = InvestorContract.objects.all().exclude(number = obj.number).aggregate(Max('number'))['number__max'] or 0    
        else: # якщо в інвестора вже є контракт
            obj.number = contracts_set[0].number #номер контракту
        # !!! тут перевірити, оскільки при повторному зберіганні збільшується на 1
        result = InvestorContractLviv.objects.all().filter(investor = obj.investor).aggregate(Max('specification_number'))['specification_number__max']
        obj.specification_number =  result + 1 if result else 1
        #print ('max_number = ', max_number )
        #obj.number = max_number+1
        
        #
        obj.save()
        #obj.bodytimetable_calc()
        #obj.status_body_calc() # видала система помилку при відсутності платежів по тілу: unsupported operand type(s) for -: 'NoneType' and 'float'
        obj.percentage_calc()
        if obj.control_number_periods() == False:
            self.message_user(request, "tttr")		

admin.site.register(InvestorContractLviv, InvestorContractAdminLviv)
			
			
			
#class MyModelAdmin(admin.ModelAdmin):
#   formfield_overrides = {
#        models.FloatField: {'widget': 'NumberInput', 'attrs': {'step':'.3'}},        
#       #models.FloatField: {'widget': TextInput(attrs={'step':'.1'})},        
#    }

#admin.site.register(MyModel, MyModelAdmin)

#class WeeklyCarReportAdmin(ExportMixin, ModelAdminTotals):
#class WeeklyCarReportAdmin(ExportMixin, admin.ModelAdmin):


class WeeklyCarReportAdminKyiv(ExportMixin, admin.ModelAdmin):
    """ Тижневий звіт по авто """
    list_display = ('date', 'client', 'car', 'amount_payment_usd', 'paid_for_the_week',  'payments_difference', 'frequency_payment' )
    list_totals = [('amount_payment_usd',  Sum)]
    list_filter = (
    ('date', DateRangeFilter), # this is a tuple
    )    
    #change_list_template = 'admin/weekly_car_report_admin_change_list.html'
    #change_list_template= 'admin/cars_rental/clientcontractweeklycarreportkyiv/change_list.html'
    #date_hierarchy = 'date'
	
	
    actions=["export_excel_test",]
	
    
	
    #def export_excel_test (self, request, queryset):
    def export_excel_test (self, request, queryset):
        #def export_users_xls(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="WeeklyCarReportAdminKyiv.xls"'
        
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Тижневий звіт по авто')
        
        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Дата контракту', 'Клієнт', 'Авто', 'Сума платежу, $', 'Оплачено за тиждень', 'Різниця', 'Періодичність оплати']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        #rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
        #rows = WeeklyCarReportAdminKyiv.list_display
        
        #print('TEST =', self.get_queryset(request))
        #print('TEST =', self.paid_for_the_week(queryset[1]))
        #rows = "test"
        #ws.write(row_num+1, col_num, rows, font_style)
        
        for obj in queryset:
            row_num += 1
            #for col_num in range(4):
            client = str(obj.client)
            car = str(obj.car)
            frequency_payment = str(obj.frequency_payment)
            ws.write(row_num, 0, obj.date, font_style)            
            ws.write(row_num, 1, client, font_style)
            ws.write(row_num, 2, car, font_style)
            ws.write(row_num, 3, obj.amount_payment_usd, font_style)
            ws.write(row_num, 4, self.paid_for_the_week(obj), font_style)
            ws.write(row_num, 5, self.payments_difference(obj), font_style)
            ws.write(row_num, 6, frequency_payment, font_style)			
            #print('TEST =', obj.client)            

			
        wb.save(response)
        return response
    export_excel_test.short_description="Export excel file"






    def paid_for_the_week(self, obj):
        """ Розрахунок суми платежів по контракту за останній тиждень, або за період """
        today=date.today()
        result =  loan_amount_paid_usd = obj.clientcontracttimetablekyiv_set.all().filter(planned_payment_date__lte=today).aggregate(Sum('amount_paid_usd'))['amount_paid_usd__sum'] or 0
        return result
    paid_for_the_week.short_description = 'Оплачено за тиждень'

    def payments_difference(self, obj):
        """ Різниця між оплаченими платежами та плановим """
        return self.paid_for_the_week(obj) - obj.amount_payment_usd
    payments_difference.short_description = 'Різниця'

    def get_total_sum(self):
        """ Розрахувати суму """
        #functions to calculate whatever you want...
        total_sum = ClientContractTimetableKyiv.objects.all().aggregate(Sum('amount_paid_usd'))['amount_paid_usd__sum']
        return total_sum

    #change_list_template = 'admin/cars_rental/extras/sometemplate_change_list.html'
    #change_list_results_template = 'admin/cars_rental/extras/change_list_results_.html'
    
    def changelist_view(self, request, extra_context=None):
    
        my_context = {
            'total': self.get_total_sum(),
        }
        return super(WeeklyCarReportAdminKyiv, self).changelist_view(request,
            extra_context=my_context)

#    """
#    def changelist_view(self, request, extra_context=None):
#        response = super().changelist_view(
#            request,
#            extra_context=extra_context,
#        )
#        response.context_data['cl']['1'] = '1'
#        
#        try:
#            qs = response.context_data['cl'].queryset
#        except (AttributeError, KeyError):
#            return response
        
        
            
#        metrics = {
#            'total': Count('id'),
#            'total_sales': Sum('initial_cost_car_usd'),
#        }
#        response.context_data['summary'] = list(
#            qs
#            .values('clientcontract__category__name')
#            .annotate(**metrics)
#            .order_by('-total_sales')
#        )
#        
#        return response
#    """

admin.site.register(ClientContractWeeklyCarReportKyiv, WeeklyCarReportAdminKyiv)



# Робота з модулем django-import-export
#class ClientResource(resources.ModelResource):
#    class Meta:
#        model = Client
#		
#@admin.register(Client)
#class ClientAdmin(ImportExportModelAdmin):
#    pass