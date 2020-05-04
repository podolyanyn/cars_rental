from django.db import models
from datetime import date, timedelta
from django.db.models import Avg, Max, Min, Sum
# Create your models here.

# Клієнт
class Client(models.Model):
    full_name = models.CharField('ПІБ', max_length=50) 									# ПІБ
    residence_address = models.CharField('адреса проживання', max_length=100)			# адреса проживання 
    registration_address = models.CharField('адреса реєстрації', max_length=100)		# адреса реєстрації
    passport_series = models.CharField('серія паспорту',max_length=2)					# серія паспорту
    passport_number = models.CharField('номер паспорту', max_length=6)					# номер паспорту
    who_issued_passport = models.CharField('ким виданий паспорт', max_length=100)		# ким виданий паспорт
    when_passport_is_issued = models.DateField('коли виданий паспорт')					# коли виданий паспорт
    rnokpp = models.CharField('реєстраційний номер облікової картки платника податків', max_length=10)		# реєстраційний номер облікової картки платника податків
    phone_number = models.CharField('номер телефону', max_length=15)										# номер телефону
    phone_number_2 = models.CharField('номер телефону 2', max_length=15, null=True)										# номер телефону 2
    phone_number_3 = models.CharField('номер телефону 3', max_length=15, null=True)										# номер телефону 3
    # ...
    def __str__(self):
        return self.full_name

class ClientOdesa(models.Model):
    full_name = models.CharField('ПІБ', max_length=50) 									# ПІБ
    residence_address = models.CharField('адреса проживання', max_length=100)			# адреса проживання 
    registration_address = models.CharField('адреса реєстрації', max_length=100)		# адреса реєстрації
    passport_series = models.CharField('серія паспорту',max_length=2)					# серія паспорту
    passport_number = models.CharField('номер паспорту', max_length=6)					# номер паспорту
    who_issued_passport = models.CharField('ким виданий паспорт', max_length=100)		# ким виданий паспорт
    when_passport_is_issued = models.DateField('коли виданий паспорт')					# коли виданий паспорт
    rnokpp = models.CharField('реєстраційний номер облікової картки платника податків', max_length=10)		# реєстраційний номер облікової картки платника податків
    phone_number = models.CharField('номер телефону', max_length=15)										# номер телефону
    # ...
    def __str__(self):
        return self.full_name
	
	
# Інвестор
class Investor(models.Model):
    full_name = models.CharField('ПІБ', max_length=50) 									# ПІБ
    phone_number = models.CharField('номер телефону', max_length=15)					# номер телефону
    # ...
    def __str__(self):
        return self.full_name
		
# Інвестор
class InvestorOdesa(models.Model):
    full_name = models.CharField('ПІБ', max_length=50) 									# ПІБ
    phone_number = models.CharField('номер телефону', max_length=15)					# номер телефону
    # ...
    def __str__(self):
        return self.full_name


		
# Колір авто		
class Color(models.Model):    
    name = models.CharField('Колір', max_length=20,  unique=True) 									# назва кольору
    # ...
    def __str__(self):
        return self.name #+ " " + str(self.id)
		
# Авто
class Car(models.Model):
    brand = models.CharField('Марка', max_length=20) 									# марка
    model = models.CharField('Модель', max_length=20)									# модель
    production_year = models.IntegerField('Рік випуску')								# рік  випуску
    car_body_number = models.CharField('Номер кузова', max_length=30)					# номер кузова
    license_plate = models.CharField('Номерний знак', max_length=30)					# номерний знак
    #car_color = models.CharField('Колір', max_length=30, null=True)						# Колір
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=1)							# Колір
    car_mileage = models.IntegerField('Пробіг', null=True)								# Пробіг    	
    # ...
    def __str__(self):
        return self.brand + " " + self.model + " " + self.license_plate
			
class CarOdesa(models.Model):
    brand = models.CharField('Марка', max_length=20) 									# марка
    model = models.CharField('Модель', max_length=20)									# модель
    production_year = models.IntegerField('Рік випуску')								# рік  випуску
    car_body_number = models.CharField('Номер кузова', max_length=30)					# номер кузова
    license_plate = models.CharField('Номерний знак', max_length=30)					# номерний знак
    # ...
    def __str__(self):
        return self.car_body_number

# Клієнтський контракт		
class ClientContract(models.Model):
    DAYS_WEEK = (
        (0, "понеділок"),
        (1, "вівторок"),
        (2, "середа"),
        (3, "четвер"),
        (4, "п'ятниця"),
    )
    contract_number = models.CharField('Номер контракту', max_length=10) 				# номер контракту
    contract_city = models.CharField('Місто, де заключений контракт', max_length=10)	# Назва міста, в якому заключений контракт !!! Доопрацювати вибір зі списку
    contract_date = models.DateField('Дата контракту')									# Дата контракту
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)			# Клієнт    
    car = models.OneToOneField(Car, on_delete=models.CASCADE, default=2)			# 	Авто
    investor_full_name = models.CharField('ПІБ інвестора',max_length=50)				# ПІБ інвестора	
    director_full_name = models.CharField('ПІБ директора фірми/філіалу фірми',max_length=50)				# ПІБ директора фірми/філіалу фірми
    client_full_name = models.CharField('ПІБ клієнта', max_length=50) 					# ПІБ клієнта
    initial_cost_car_usd = models.FloatField('Вартість автомобіля в доларах, на момент складання контракту')# Вартість автомобіля в доларах, на момент складання контракту
    commercial_course_usd = models.FloatField('Комерційний курс долара', null=True)		# Комерційний курс долара
    initial_cost_car_uah = models.FloatField('Вартість автомобіля в гривні, на момент складання контракту') # Вартість автомобіля в гривні, на момент складання контракту; автоматичний перерахунок, поле не редагується
    contract_period_days = models.IntegerField('Строк контракту, в днях') 				# Строк контракту, в днях
    #contract_period_years = models.IntegerField('Строк контракту, в роках') 			# Строк контракту, в роках
    #frequency_payment = models.CharField('Періодичність оплати', max_length=10)			# Періодичність оплати
    frequency_payment = models.IntegerField('Періодичність оплати', choices = DAYS_WEEK)			# Періодичність оплати
    amount_payment_usd = models.FloatField('Сума платежу в доларах') 					# Сума платежу в доларах    
    amount_payment_uah = models.FloatField('Сума платежу в гривнях', null=True)			# Сума платежу в гривнях; автоматичний перерахунок, поле не редагується	
    # ...
    def __str__(self):
        return self.contract_number
	# Розрахунок графіку погашення
    def timetable_calc(self): 
        #if self.clientcontracttimetable_set.count() > 0:
         #  return
        #else:
        #today = date.today()
            for i in range(7) :
                day0 = self.contract_date + timedelta(days=i)
                if day0.weekday() == self.frequency_payment:
                    day_1 = day0
                    break
            i = day_1
            day_end = self.contract_date + timedelta(days=self.contract_period_days)
            while i <= day_end:
                self.clientcontracttimetable_set.create(planned_payment_date = i, planned_amount_payment_usd=self.amount_payment_usd, real_payment_date=i, amount_paid_usd=self.amount_payment_usd)
                i = i + timedelta(days=7)

		
# Клієнтський контракт, графік погашення	(тіло + %)	
class ClientContractTimetable(models.Model):
    client_contract = models.ForeignKey(ClientContract, on_delete=models.CASCADE, default=1)		# клієнтський контракт
    planned_payment_date = models.DateField('Планова дата платежу', null=True)							# Планова дата платежу
    planned_amount_payment_usd = models.FloatField('Планова сума платежу, в доларах', null=True)							# Планова сума платежу, в доларах
    real_payment_date = models.DateField('Дійсна дата платежу', null=True)									# Дійсна дата платежу
    amount_paid_usd = models.FloatField('Оплачена сума, в доларах', null=True) 											# Оплачена сума, в доларах
    # ...
    #def __str__(self):
    #   return self.contract_number
		
		
class ClientContractOdesa(models.Model):
    contract_number = models.CharField('Номер контракту', max_length=10) 				# номер контракту
    contract_city = models.CharField('Місто, де заключений контракт', max_length=10)	# Назва міста, в якому заключений контракт !!! Доопрацювати вибір зі списку
    contract_date = models.DateField('Дата контракту')									# Дата контракту
    investor_full_name = models.CharField('ПІБ інвестора',max_length=50)				# ПІБ інвестора	
    director_full_name = models.CharField('ПІБ директора фірми/філіалу фірми',max_length=50)				# ПІБ директора фірми/філіалу фірми
    client_full_name = models.CharField('ПІБ клієнта', max_length=50) 					# ПІБ клієнта
    initial_cost_car_usd = models.FloatField('Вартість автомобіля в доларах, на момент складання контракту')# Вартість автомобіля в доларах, на момент складання контракту
    initial_cost_car_uah = models.FloatField('Вартість автомобіля в гривні, на момент складання контракту') # Вартість автомобіля в гривні, на момент складання контракту
    contract_period_days = models.IntegerField('Строк контракту, в днях') 				# Строк контракту, в днях
    contract_period_years = models.IntegerField('Строк контракту, в роках') 			# Строк контракту, в роках
    frequency_payment = models.CharField('Періодичність оплати', max_length=10)			# Періодичність оплати
    amount_payment_usd = models.FloatField('Сума платежу в доларах') 					# Сума платежу в доларах
    # ...
    def __str__(self):
        return self.contract_number
		
# Інвесторський контракт		
class InvestorContract(models.Model):
    contract_number = models.CharField('Номер контракту', max_length=10) 				# номер контракту
    contract_city = models.CharField('Місто, де заключений контракт', max_length=10)	# Назва міста, в якому заключений контракт !!! Доопрацювати вибір зі списку
    contract_date = models.DateField('Дата контракту')									# Дата контракту
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, default=1)			# Інвестор    
    investor_full_name = models.CharField('ПІБ інвестора',max_length=50)				# ПІБ інвестора	
    director_full_name = models.CharField('ПІБ директора фірми/філіалу фірми',max_length=50)				# ПІБ директора фірми/філіалу фірми
    client_full_name = models.CharField('ПІБ клієнта', max_length=50) 					# ПІБ клієнта
    car = models.OneToOneField(Car, on_delete=models.CASCADE, default=2)			# 	Авто
    initial_cost_car_usd = models.FloatField('Вартість автомобіля в доларах, на момент складання контракту')# Вартість автомобіля в доларах, на момент складання контракту
    initial_cost_car_uah = models.FloatField('Вартість автомобіля в гривні, на момент складання контракту') # Вартість автомобіля в гривні, на момент складання контракту
    contract_period_days = models.IntegerField('Строк контракту, в днях') 				# Строк контракту, в днях
    #contract_period_years = models.IntegerField('Строк контракту, в роках') 			# Строк контракту, в роках
    #frequency_payment = models.CharField('Періодичність оплати', max_length=10)		# Періодичність оплати
    #amount_payment_usd = models.FloatField('Сума платежу в доларах') 					# Сума платежу в доларах; 17.04.2020 пробував закоментити, видавало помилки при міграції, цікаво чому ???
    number_periods = models.IntegerField('Кількість періодів', default=4) 				# Кількість періодів
    status_body = models.FloatField('Стан розрахунку по тілу кредита. Переплата/прострочка (-)', null=True) 					# Стан розрахунку по тілу кредита. Переплата/прострочка (-)
	#status_percentage = models.FloatField('Стан розрахунку по відсотках кредиту. Переплата/прострочка (-)', null=True) 					# Стан розрахунку по тілу кредита. Переплата/прострочка (-)
    іnterest_rate = models.FloatField('Процентна ставка', null=True) 								# Процентна ставка
    period_1 = models.DateField('Кінцева дата погашення (період 1)', null=True)																# Період 1, тобто перших пів-року
    period_1_percentage = models.FloatField('Частина основного боргу, у відсотках (період 1)', default=0) 											# Відсоток на період 1
    period_2 = models.DateField('Кінцева дата погашення (період 2)', null=True)																# Період 2
    period_2_percentage = models.FloatField('Частина основного боргу, у відсотках (період 2)', default=0) 											# Відсоток на період 2
    period_3 = models.DateField('Кінцева дата погашення (період 3)', null=True)																# Період 3
    period_3_percentage = models.FloatField('Частина основного боргу, у відсотках (період 3)', default=0) 											# Відсоток на період 3
    period_4 = models.DateField('Кінцева дата погашення (період 4)', null=True)																# Період 4
    period_4_percentage = models.FloatField('Частина основного боргу, у відсотках (період 4)', default=0) 											# Відсоток на період 4     
	# ...
    def __str__(self):
        return self.contract_number
    def bodytimetable_calc(self): 
        #self.investorcontractbodytimetable_set.create(period = self.period_1, period_percentage = self.period_1_percentage, period_percentage_usd = self.period_1_percentage / 100 * self.initial_cost_car_usd)		
        self.investorcontractbodytimetable_set.update(period_percentage_usd = period_percentage / 100 * self.initial_cost_car_usd)		
        #
    #  розрахунок status_body
    def status_body_calc(self):
        today=date.today()
        timetable=self.investorcontractbodytimetable_set.all()
        #print('timetable.aggregate  = ', timetable.all().aggregate(Sum('period_percentage_usd')) )
        #timetable=self.investorcontractbodytimetable_set.objects.all()
        #kkk = self.investorcontractbodytimetable_set.count()
        #kkk=self.investorcontractbodytimetable_set.count()
        if today <= timetable[0].period:
            self.status_body = self.investorcontractbodypayment_set.all().aggregate(Sum('sum'))['sum__sum']            
			#self.refresh_from_db()
			#self.status_body.update(self.investorcontractbodypayment_set.all().aggregate(Sum('sum')))
            #print("self.status_body = ", self.status_body)
        else:
            if today > timetable[self.number_periods-1].period:
                self.status_body = self.investorcontractbodypayment_set.all().aggregate(Sum('sum'))['sum__sum'] -  timetable.aggregate(Sum('period_percentage_usd'))['period_percentage_usd__sum']
            else:
                for i in 	range(self.number_periods-1):
                    if timetable[i].period<today<=timetable[i+1].period :
                        break
                print('i = ', i)
                print('timetable[i].period = ', timetable[i].period, "type = ", type(timetable[i].period))
                #print ('self.investorcontractbodypayment_set.date = ', self.investorcontractbodypayment_set.date)
                self.status_body = self.investorcontractbodypayment_set.all().filter(date__lte=timetable[i].period).aggregate(Sum('sum'))['sum__sum'] -  timetable.filter(period__lte=timetable[i].period).aggregate(Sum('period_percentage_usd'))['period_percentage_usd__sum']
                #self.status_body = self.investorcontractbodypayment_set.all().filter(date<=timetable[i].period).aggregate(Sum('sum'))['sum__sum'] -  timetable.aggregate(Sum('period_percentage_usd'))['period_percentage_usd__sum']
        self.save()
        #
    def control_number_periods(self):
        timetable=self.investorcontractbodytimetable_set.all()
        if self.investorcontractbodytimetable_set.count() > self.number_periods:
            #print ('karaul')
            #self.message_user(request, "tttr")
            return False
    #    
                                  			 
# Інвесторський контракт, графік погашення	тіла кредиту		
# Це саме графік погашення тіла, платежі будуть винесені в окрему таблицю
class InvestorContractBodyTimetable(models.Model):
    investor_contract = models.ForeignKey(InvestorContract, on_delete=models.CASCADE, default=1)		# інвесторський контракт
    period = models.DateField('Планова кінцева дата погашення', null=True)																# Період 1, тобто перших пів-року
    period_percentage = models.FloatField('Частина основного боргу, у відсотках', default=0) 	
    period_percentage_usd = models.FloatField('Частина основного боргу, у доларах', default = 0) 	    
    #real_payment_date = models.DateField('Дійсна дата платежу', null=True)									# Дійсна дата платежу
    #amount_paid_usd = models.FloatField('Оплачена сума, в доларах', null=True) 											# Оплачена сума, в доларах
    # ...
    #def __str__(self):
    #   return self.contract_number
    class Meta:
        ordering = ['period']

# Інвесторський контракт, платежі по тілу кредиту
class InvestorContractBodyPayment(models.Model):
    investor_contract = models.ForeignKey(InvestorContract, on_delete=models.CASCADE, default=1)		# інвесторський контракт
    date = models.DateField('Дата платежу', null=True)																# Дата платежу
    sum = models.FloatField('Сума платежу (погашення тіла боргу)', default=0) 							# Сума платежу (погашення тіла боргу)
		
# Інвесторський контракт, платежі по % на тіло кредиту
class InvestorContractPercentagePayment(models.Model):
    investor_contract = models.ForeignKey(InvestorContract, on_delete=models.CASCADE, default=1)		# інвесторський контракт
    planned_payment_date = models.DateField('Планова дата платежу', null=True)							# Планова дата платежу
    planned_amount_payment_usd = models.FloatField('Планова сума платежу, в доларах', null=True)							# Планова сума платежу, в доларах
    real_payment_date = models.DateField('Дійсна дата платежу', null=True)									# Дійсна дата платежу
    amount_paid_usd = models.FloatField('Оплачена сума, в доларах', null=True) 											# Оплачена сума, в доларах
    # ...
    #def __str__(self):
    #   return self.contract_number
	

	

		
class InvestorContractOdesa(models.Model):
    contract_number = models.CharField('Номер контракту', max_length=10) 				# номер контракту
    contract_city = models.CharField('Місто, де заключений контракт', max_length=10)	# Назва міста, в якому заключений контракт !!! Доопрацювати вибір зі списку
    contract_date = models.DateField('Дата контракту')									# Дата контракту
    investor_full_name = models.CharField('ПІБ інвестора',max_length=50)				# ПІБ інвестора	
    director_full_name = models.CharField('ПІБ директора фірми/філіалу фірми',max_length=50)				# ПІБ директора фірми/філіалу фірми
    client_full_name = models.CharField('ПІБ клієнта', max_length=50) 					# ПІБ клієнта
    initial_cost_car_usd = models.FloatField('Вартість автомобіля в доларах, на момент складання контракту')# Вартість автомобіля в доларах, на момент складання контракту
    initial_cost_car_uah = models.FloatField('Вартість автомобіля в гривні, на момент складання контракту') # Вартість автомобіля в гривні, на момент складання контракту
    contract_period_days = models.IntegerField('Строк контракту, в днях') 				# Строк контракту, в днях
    contract_period_years = models.IntegerField('Строк контракту, в роках') 			# Строк контракту, в роках
    frequency_payment = models.CharField('Періодичність оплати', max_length=10)			# Періодичність оплати
    amount_payment_usd = models.FloatField('Сума платежу в доларах') 					# Сума платежу в доларах
    # ...
    def __str__(self):
        return self.contract_number


		
#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)