from django.contrib import admin
from django.db.models import Max
from datetime import date

# Register your models here.
from .models import Client, Investor, Car, ClientContract, InvestorContract, Color, ClientContractTimetable, InvestorContractPercentagePayment, InvestorContractBodyTimetable
from .models import InvestorContractBodyPayment, ClientContractTO, Branch, ExchangeRateKyiv, ExchangeRateLviv, ExchangeRateOdesa
#from .models import ClientOdesa, InvestorOdesa, CarOdesa, ClientContractOdesa, InvestorContractOdesa

#from .models import ClientOdesa
#from .models import Investor
#from .models import InvestorOdesa
#from .models import Car
#from .models import CarOdesa
#from .models import ClientContract
#from .models import ClientContractOdesa
#from .models import InvestorContract
#from .models import InvestorContractOdesa

#admin.site.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # 24.04 Зміна шаблону. Правда, чомусь для всіх об'єктів цей шаблон підтягнувся, не лише для клієнта.
    # change_form_template = 'admin/change_form.html'	
    list_display = ('full_name', 'phone_number', 'phone_number_2', 'phone_number_3')
    search_fields = ['full_name', 'phone_number', 'phone_number_2', 'phone_number_3']
admin.site.register(Client, ClientAdmin)

#admin.site.register(ClientOdesa)

#admin.site.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')
    search_fields = ['full_name', 'phone_number']
admin.site.register(Investor, InvestorAdmin)

#admin.site.register(InvestorOdesa)


class CarAdmin(admin.ModelAdmin):
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
admin.site.register(Car, CarAdmin)

#admin.site.register(CarOdesa)

class CarInline(admin.StackedInline):
    model = Car
    #extra = 1
class ClientInline(admin.StackedInline):
    model = Client
    #extra = 1
class ClientContractTimetableInline(admin.TabularInline):
    model = ClientContractTimetable
    extra = 0
    fields = ['planned_payment_date', 'planned_amount_payment_usd', 'real_payment_date', 'amount_paid_usd']
    readonly_fields = ['planned_payment_date', 'planned_amount_payment_usd']
class ClientContractTOInline(admin.TabularInline):
    model = ClientContractTO
    extra = 0
    fields = ['date', 'sum']
class ClientContractAdmin(admin.ModelAdmin):
    #fieldsets = [
    #   (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    inlines = [ClientContractTOInline, ClientContractTimetableInline]	
    #inlines = [ClientInline]
	# ...
    list_display = ('number', 'city', 'date', 'client', 'car')
    #list_editable = ('city', 'date', 'client', 'initial_cost_car_usd', 'commercial_course_usd', 'initial_cost_car_uah', 'period_days')
    #list_filter = ['brand', 'model']
    #search_fields = [ 'client', 'car']
    search_fields = [ 'number', 'client__full_name',  'car__license_plate']
    #date_hierarchy = 'pub_date'
    def save_model(self, request, obj, form, change):
        obj.save()
        obj.timetable_calc()
        obj.to_calc()
           #obj.user = request.user
        #super().save_model(request, obj, form, change)
        #self.clientcontracttimetable_set.create(planned_amount_payment_usd=222)
        #super().test()
        #super().save_model(request, obj, form, change)
    def get_changeform_initial_data(self, request):
        #return {'number': '100'}
        # return obj.number_calc()
        #self.status_body = self.investorcontractbodypayment_set.all().filter(date__lte=timetable[i].payment_date).aggregate(Sum('sum'))['sum__sum']
        #sss = self.all().aggregate(Max('number_number'))
        # Розрахунок максимального номеру в поточному році. Використав скорочену форму терн. оператора. Якщо отримую None, то присвоюю 0
        max_number = ClientContract.objects.all().filter(date__year = date.today().year).aggregate(Max('number_number'))['number_number__max'] or 0
        print ('max_number = ', max_number)		
        return {'number': str(date.today().year) + '-' + str(max_number+1) + '/К', 'number_number':max_number+1}
        		
admin.site.register(ClientContract, ClientContractAdmin)


class InvestorContractPercentagePaymentInline(admin.TabularInline):
    model = InvestorContractPercentagePayment
    extra = 0
    fields = ['date', 'sum']
    #readonly_fields = ['planned_payment_date', 'planned_amount_payment_usd']

class InvestorContractBodyTimetableInline(admin.TabularInline):
    model = InvestorContractBodyTimetable
    extra = 0
    #can_delete = False
    fields = ['payment_date', 'payment_percentage', 'payment_usd']
    #readonly_fields = ['payment_usd']


class InvestorContractBodyPaymentInline(admin.TabularInline):
    model = InvestorContractBodyPayment
    extra = 0
    #can_delete = False
    fields = ['date', 'sum']
    #readonly_fields = ['payment_usd']
	
class InvestorContractAdmin(admin.ModelAdmin):
    #fieldsets = [
    #   (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    fields = ('number', 'specification_number', 'city', 'date', 'investor',  'director_full_name', 'client_full_name', 'car', 'initial_cost_car_usd', 'initial_cost_car_uah', 'period_days', 'number_periods', 'status_body', 'іnterest_rate', 'last_month_percentage', 'status_percentage')
    inlines = [InvestorContractBodyTimetableInline, InvestorContractBodyPaymentInline, InvestorContractPercentagePaymentInline]
    #inlines = [InvestorContractPercentagePaymentInline]
    #inlines = [ClientInline]
	# ...
    list_display = ('number', 'specification_number', 'city', 'date', 'investor', 'car')
    #list_editable = ('city', 'date', 'client', 'initial_cost_car_usd', 'commercial_course_usd', 'initial_cost_car_uah', 'period_days')
    #list_filter = ['brand', 'model']
    #search_fields = [ 'client', 'car']
    search_fields = [ 'number', 'investor__full_name',  'car__license_plate']
    #date_hierarchy = 'pub_date'
    def save_model(self, request, obj, form, change):
        # (ПЕРЕВІРИТИ ВЕСЬ РОЗРАХУНОК !!!) Розрахунок номеру контракту та номеру специфікації для даного клієнта
        # Визначаємо, чи в даного інвестора взагалі є контракти 
        contracts_set = InvestorContract.objects.all().filter(investor = obj.investor)
        print ('contracts_set = ', contracts_set )
        if not contracts_set.exists():
            obj.number = InvestorContract.objects.all().aggregate(Max('number'))['number__max'] + 1    
            # Не враховуємо номер контракту даного об'єкту, інакше при зберіганні він його постійно збільшуватиме +1 (??? порібно подумати)
            #contract_max_number = InvestorContract.objects.all().exclude(number = obj.number).aggregate(Max('number'))['number__max'] or 0    
        else: # якщо в інвестора вже є контракт
            obj.number = contracts_set[0].number #номер контракту
            # !!! тут перевірити, оскільки при повторному зберіганні збільшується на 1
            obj.specification_number = InvestorContract.objects.all().filter(investor = obj.investor).aggregate(Max('specification_number'))['specification_number__max'] + 1 or 1
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
admin.site.register(InvestorContract, InvestorContractAdmin)

#admin.site.register(ClientContractOdesa)


#admin.site.register(InvestorContractOdesa)
admin.site.register(Color)
admin.site.register(Branch)
#admin.site.register(ExchangeRateKyiv)

class ExchangeRateKyivAdmin(admin.ModelAdmin):
    list_display = ('date', 'sum')    
admin.site.register(ExchangeRateKyiv, ExchangeRateKyivAdmin)

class ExchangeRateLvivAdmin(admin.ModelAdmin):
    list_display = ('date', 'sum')    
admin.site.register(ExchangeRateLviv, ExchangeRateLvivAdmin)

class ExchangeRateOdesaAdmin(admin.ModelAdmin):
    list_display = ('date', 'sum')    
admin.site.register(ExchangeRateOdesa, ExchangeRateOdesaAdmin)