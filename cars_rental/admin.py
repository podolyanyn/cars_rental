from django.contrib import admin

# Register your models here.
from .models import Client, Investor, Car, ClientContract, InvestorContract, Color, ClientContractTimetable, InvestorContractTimetable
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

admin.site.register(Client)
#admin.site.register(ClientOdesa)
admin.site.register(Investor)
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
admin.site.register(ClientContract, ClientContractAdmin)


class InvestorContractTimetableInline(admin.TabularInline):
    model = InvestorContractTimetable
    extra = 0
    fields = ['planned_payment_date', 'planned_amount_payment_usd', 'real_payment_date', 'amount_paid_usd']
    readonly_fields = ['planned_payment_date', 'planned_amount_payment_usd']

class InvestorContractAdmin(admin.ModelAdmin):
    #fieldsets = [
    #   (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    inlines = [InvestorContractTimetableInline]
    #inlines = [ClientInline]
	# ...
    list_display = ('contract_number', 'contract_city', 'contract_date', 'investor', 'car')
    #list_editable = ('contract_city', 'contract_date', 'client', 'initial_cost_car_usd', 'commercial_course_usd', 'initial_cost_car_uah', 'contract_period_days')
    #list_filter = ['brand', 'model']
    #search_fields = [ 'client', 'car']
    search_fields = [ 'contract_number', 'investor__full_name',  'car__license_plate']
    #date_hierarchy = 'pub_date'
admin.site.register(InvestorContract, InvestorContractAdmin)

#admin.site.register(ClientContractOdesa)


#admin.site.register(InvestorContractOdesa)
admin.site.register(Color)