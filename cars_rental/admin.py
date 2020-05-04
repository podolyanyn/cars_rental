from django.contrib import admin

# Register your models here.
from .models import Client, Investor, Car, ClientContract, InvestorContract, Color, ClientContractTimetable, InvestorContractPercentagePayment, InvestorContractBodyTimetable, InvestorContractBodyPayment
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
    list_display = ('brand', 'model', 'production_year', 'car_body_number', 'license_plate', 'color', 'car_mileage')
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
class ClientContractAdmin(admin.ModelAdmin):
    #fieldsets = [
    #   (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    inlines = [ClientContractTimetableInline]	
    #inlines = [ClientInline]
	# ...
    list_display = ('contract_number', 'contract_city', 'contract_date', 'client', 'car')
    #list_editable = ('contract_city', 'contract_date', 'client', 'initial_cost_car_usd', 'commercial_course_usd', 'initial_cost_car_uah', 'contract_period_days')
    #list_filter = ['brand', 'model']
    #search_fields = [ 'client', 'car']
    search_fields = [ 'contract_number', 'client__full_name',  'car__license_plate']
    #date_hierarchy = 'pub_date'
    def save_model(self, request, obj, form, change):
        obj.save()
        obj.timetable_calc()
           #obj.user = request.user
        #super().save_model(request, obj, form, change)
        #self.clientcontracttimetable_set.create(planned_amount_payment_usd=222)
        #super().test()
        #super().save_model(request, obj, form, change)
admin.site.register(ClientContract, ClientContractAdmin)


class InvestorContractPercentagePaymentInline(admin.TabularInline):
    model = InvestorContractPercentagePayment
    extra = 0
    fields = ['planned_payment_date', 'planned_amount_payment_usd', 'real_payment_date', 'amount_paid_usd']
    readonly_fields = ['planned_payment_date', 'planned_amount_payment_usd']

class InvestorContractBodyTimetableInline(admin.TabularInline):
    model = InvestorContractBodyTimetable
    extra = 0
    #can_delete = False
    fields = ['period', 'period_percentage', 'period_percentage_usd']
    #readonly_fields = ['period_percentage_usd']


class InvestorContractBodyPaymentInline(admin.TabularInline):
    model = InvestorContractBodyPayment
    extra = 0
    #can_delete = False
    fields = ['date', 'sum']
    #readonly_fields = ['period_percentage_usd']
	
class InvestorContractAdmin(admin.ModelAdmin):
    #fieldsets = [
    #   (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    fields = ('contract_number', 'contract_city', 'contract_date', 'investor', 'investor_full_name', 'director_full_name', 'client_full_name', 'car', 'initial_cost_car_usd', 'initial_cost_car_uah', 'contract_period_days', 'number_periods', 'status_body',('period_1', 'period_1_percentage'), ('period_2', 'period_2_percentage'), ('period_3', 'period_3_percentage'), ('period_4', 'period_4_percentage'))
    inlines = [InvestorContractBodyTimetableInline, InvestorContractBodyPaymentInline, InvestorContractPercentagePaymentInline]
    #inlines = [InvestorContractPercentagePaymentInline]
    #inlines = [ClientInline]
	# ...
    list_display = ('contract_number', 'contract_city', 'contract_date', 'investor', 'car')
    #list_editable = ('contract_city', 'contract_date', 'client', 'initial_cost_car_usd', 'commercial_course_usd', 'initial_cost_car_uah', 'contract_period_days')
    #list_filter = ['brand', 'model']
    #search_fields = [ 'client', 'car']
    search_fields = [ 'contract_number', 'investor__full_name',  'car__license_plate']
    #date_hierarchy = 'pub_date'
    def save_model(self, request, obj, form, change):
        obj.save()
        #obj.bodytimetable_calc()
        obj.status_body_calc()
        if obj.control_number_periods() == False:
            self.message_user(request, "tttr")		

admin.site.register(InvestorContract, InvestorContractAdmin)

#admin.site.register(ClientContractOdesa)


#admin.site.register(InvestorContractOdesa)
admin.site.register(Color)