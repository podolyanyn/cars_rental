from django.db import models
from datetime import date, timedelta
from django.db.models import Avg, Max, Min, Sum
from django.utils import timezone
# Create your models here.

#Відділення
class Branch(models.Model):
    city = models.CharField('Місто', max_length=25) 									# Місто
    def __str__(self):
        return self.city
		
    class Meta:        
        verbose_name = "Відділення"
        verbose_name_plural = "Відділення"

# Валютний курс
class ExchangeRate(models.Model):
    date = models.DateField('Дата', null=True, unique = True)							# Дата 
    sum = models.FloatField('Курс, 1$ = (грн) ', null=True) 		# Курс 
	
    def __str__(self):
        return str(self.sum)
    class Meta:
        abstract = True	

		
class ExchangeRateKyiv(ExchangeRate):
	# Отримати курс на сьогодні
    #def today_exchange_rate():
     #   return {'date': date.today()}
	 
    class Meta:        
        verbose_name = "Валютний курс (Київ)"
        verbose_name_plural = "Валютний курс (Київ)"
		
class ExchangeRateLviv(ExchangeRate):
    class Meta:        
        verbose_name = "Валютний курс (Львів)"
        verbose_name_plural = "Валютний курс (Львів)"
	
class ExchangeRateOdesa(ExchangeRate):

    class Meta:        
        verbose_name = "Валютний курс (Одеса)"
        verbose_name_plural = "Валютний курс (Одеса)"
		
# Колір авто		
class Color(models.Model):    
    name = models.CharField('Колір', max_length=20,  unique=True) 									# назва кольору
    # ...
    def __str__(self):
        return self.name #+ " " + str(self.id)

    class Meta:        
        verbose_name = "Колір авто"
        verbose_name_plural = "Кольори авто"

# Авто
class Car(models.Model):
    brand = models.CharField('Марка', max_length=20) 									# марка
    model = models.CharField('Модель', max_length=20)									# модель
    production_year = models.IntegerField('Рік випуску')								# рік  випуску
    body_number = models.CharField('Номер кузова', max_length=30)					# номер кузова
    license_plate = models.CharField('Номерний знак', max_length=30)					# номерний знак
    #car_color = models.CharField('Колір', max_length=30, null=True)						# Колір
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=1)							# Колір
    mileage = models.IntegerField('Пробіг', null=True)								# Пробіг    	
    # ...
    def __str__(self):
        return self.brand + " " + self.model + " " + self.license_plate

    class Meta:    
        abstract = True	    
        verbose_name = "Автомобіль"
        verbose_name_plural = "Автомобілі"

# Авто, Київ	
class CarKyiv(Car):  
							
    class Meta:        
        verbose_name = "Автомобіль (Київ)"
        verbose_name_plural = "Автомобілі (Київ)"

# Авто, Львів	
class CarLviv(Car):  
							
    class Meta:        
        verbose_name = "Автомобіль (Львів)"
        verbose_name_plural = "Автомобілі (Львів)"

# Клієнт
class Client(models.Model):
    full_name = models.CharField('ПІБ', max_length=50) 									# ПІБ
    residence_address = models.CharField('адреса проживання', max_length=100)			# адреса проживання 
    registration_address = models.CharField('адреса реєстрації', max_length=100)		# адреса реєстрації
    #passport_series = models.CharField('серія паспорту',max_length=2)					# серія паспорту
    #passport_number = models.CharField('номер паспорту', max_length=6)					# номер паспорту
    passport_data = models.CharField('дані  паспорту (серія + номер), чи іншого документу', max_length=10, null=True)					# дані  паспорту (серія + номер), чи іншого документу
    who_issued_passport = models.CharField('ким виданий паспорт', max_length=100)		# ким виданий паспорт
    when_passport_is_issued = models.DateField('коли виданий паспорт')					# коли виданий паспорт
    rnokpp = models.CharField('реєстраційний номер облікової картки платника податків', max_length=10)		# реєстраційний номер облікової картки платника податків
    phone_number = models.CharField('номер телефону', max_length=15)										# номер телефону
    phone_number_2 = models.CharField('номер телефону 2', max_length=15, null=True, blank=True)										# номер телефону 2
    phone_number_3 = models.CharField('номер телефону 3', max_length=15, null=True, blank=True)										# номер телефону 3
    # ...
    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True		
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"
		
# Клієнт, Київ	
class ClientKyiv(Client):  

    class Meta:        
        verbose_name = "Клієнт (Київ)"
        verbose_name_plural = "Клієнти (Київ)"

# Клієнт, Львів	
class ClientLviv(Client):  

    class Meta:        
        verbose_name = "Клієнт (Львів)"
        verbose_name_plural = "Клієнти (Львів)"
		
# Клієнтський контракт		
class ClientContract(models.Model):
		
    DAYS_WEEK = (
        (0, "понеділок"),
        (1, "вівторок"),
        (2, "середа"),
        (3, "четвер"),
        (4, "п'ятниця"),
		(5, "субота"),
    )
    number = models.CharField('Номер контракту', max_length=10) 				# номер контракту
    number_number = models.IntegerField('Номер номеру контракту', null = True)	# номер номеру контракту ), власне сам порядковий номер 1, 2, .. від початку року
    city = models.CharField('Місто, де заключений контракт', max_length=10)	# Назва міста, в якому заключений контракт !!! Доопрацювати вибір зі списку
    date = models.DateField('Дата контракту')									# Дата контракту
    client = models.ForeignKey(ClientKyiv, on_delete=models.CASCADE, default=1)			# Клієнт    
    car = models.OneToOneField(CarKyiv, on_delete=models.CASCADE, default=1)			# 	Авто
    investor_full_name = models.CharField('ПІБ інвестора',max_length=50)				# ПІБ інвестора	
    director_full_name = models.CharField('ПІБ директора фірми/філіалу фірми',max_length=50)				# ПІБ директора фірми/філіалу фірми
    #client_full_name = models.CharField('ПІБ клієнта', max_length=50) 					# ПІБ клієнта
    initial_cost_car_usd = models.FloatField('Вартість автомобіля в доларах, на момент складання контракту')# Вартість автомобіля в доларах, на момент складання контракту
    #commercial_course_usd = models.FloatField('Комерційний курс долара', null=True) #, limit_choices_to={'date': date})		# Комерційний курс долара
    #commercial_course_usd_test = models.ForeignKey(ExchangeRateKyiv, on_delete=models.CASCADE, null=True) #, limit_choices_to={'date': date})		# Комерційний курс долара
    commercial_course_usd_test = models.FloatField('Комерційний курс долара test', default = 0) #, limit_choices_to={'date': date})		# Комерційний курс долара
    initial_cost_car_uah = models.FloatField('Вартість автомобіля в гривні, на момент складання контракту', default = 0) # Вартість автомобіля в гривні, на момент складання контракту; автоматичний перерахунок, поле не редагується
    period_days = models.IntegerField('Строк контракту, в днях') 				# Строк контракту, в днях
    #period_years = models.IntegerField('Строк контракту, в роках') 			# Строк контракту, в роках
    #frequency_payment = models.CharField('Періодичність оплати', max_length=10)			# Періодичність оплати
    frequency_payment = models.IntegerField('Періодичність оплати', choices = DAYS_WEEK, default = 0)			# Періодичність оплати
    amount_payment_usd = models.FloatField('Сума платежу в доларах') 					# Сума платежу в доларах    
    amount_payment_uah = models.FloatField('Сума платежу в гривнях', default = 0)			# Сума платежу в гривнях; автоматичний перерахунок, поле не редагується
    
    loan_amount_paid_usd = models.FloatField('Сума виплачених платежів', default = 0, null = True)										#Сума виплачених платежів (Було - Виплачена сума кредиту)
    loan_amount_to_be_paid_usd = models.FloatField('Сума платежів до оплати', default = 0, null = True)								#Сума платежів до оплати (Було - Cума кредиту до оплати)
    status_body_usd = models.FloatField('Стан розрахунку по платежах. Переплата/прострочка (-)', default = 0, null = True) 	# Стан розрахунку по платежам. Переплата/прострочка (-) (Було - Стан розрахунку по кредиту. Переплата/прострочка (-))
    
    amount_payment_TO_uah = models.FloatField('Сума на ТО, в гривнях', default = 0, null = True)			# Сума платежу в гривнях на ТО
    balance_TO_uah = models.FloatField('Залишок по ТО, в гривнях', default = 0, null = True)			# Залишок по ТО, в гривнях (надходження - видатки)
    # ...
    # ...
    def __str__(self):
        return self.number
		
    class Meta:
        abstract = True	
        verbose_name = "Клієнтський контракт"
        verbose_name_plural = "Клієнтські контракти"
		
    # отримання курсу долара та перерахунок вартості авто на грн.
    def get_commercial_course_usd_test(self):
        #ExchangeRateKyiv.objects.all().filter(date = self.date): # Queryset повертає True, якщо у результаті вибірки є хоча б один елемент
        self.commercial_course_usd_test = ExchangeRateKyiv.objects.all().filter(date = self.date)[0].sum if ExchangeRateKyiv.objects.all().filter(date = self.date) else 0
        self.initial_cost_car_uah = self.initial_cost_car_usd * self.commercial_course_usd_test
        self.amount_payment_uah = self.amount_payment_usd * self.commercial_course_usd_test
        self.save()
    
    # Розрахунок графіку погашення
    def timetable_calc(self): 
        if self.clientcontracttimetablekyiv_set.count() > 0:
            return
        else:
            #today = date.today()
            for i in range(7) :
                day0 = self.date + timedelta(days=i)
                if day0.weekday() == self.frequency_payment:
                    day_1 = day0 if day0 != self.date else  self.date + timedelta(days=7)
                    break
            i = day_1
            day_end = self.date + timedelta(days=self.period_days)
            while i <= day_end:
                #self.clientcontracttimetable_set.create(planned_payment_date = i, planned_amount_payment_usd=self.amount_payment_usd, real_payment_date=i, amount_paid_usd=self.amount_payment_usd)
                self.clientcontracttimetablekyiv_set.create(planned_payment_date = i, planned_amount_payment_usd=self.amount_payment_usd, amount_paid_usd=None)
                i = i + timedelta(days=7)
                
    # Розрахунок залишку ТО
    def to_calc(self):
        self.balance_TO_uah = self.clientcontracttokyiv_set.all().aggregate(Sum('sum'))['sum__sum']
        self.save()
    
    # Розрахунок номера контракту
    #def number_calc():
    #    return {'number': '200'}
	
    def calc_loan_amount_paid(self):
        """ Розрахунок виплаченої суми кредиту та залишку по кредиту """
    
        today=date.today()
        #self.loan_amount_paid_usd = self.clientcontracttimetable_set.all().filter(real_payment_date__lte=today).aggregate(Sum('amount_paid_usd'))['amount_paid_usd__sum']
        self.loan_amount_paid_usd = self.clientcontracttimetablekyiv_set.all().filter(planned_payment_date__lte=today).aggregate(Sum('amount_paid_usd'))['amount_paid_usd__sum'] or 0
        self.loan_amount_to_be_paid_usd = self.initial_cost_car_usd - self.loan_amount_paid_usd
        self.save()

# Клієнтський контракт	, Київ	
class ClientContractKyiv(ClientContract):
    #client = None
    #car = None
    #client = models.ForeignKey(ClientKyiv, on_delete=models.CASCADE, default=1)			# Клієнт    
    #car = models.OneToOneField(CarKyiv, on_delete=models.CASCADE, default=1)			# 	Авто

    class Meta:        
        verbose_name = "Клієнтський контракт (Київ)"
        verbose_name_plural = "Клієнтські контракти (Київ)"

# Клієнтський контракт	, Львів	
class ClientContractLviv(ClientContract):
    client = models.ForeignKey(ClientLviv, on_delete=models.CASCADE, default=1)			# Клієнт    
    car = models.OneToOneField(CarLviv, on_delete=models.CASCADE, default=1)			# 	Авто

    class Meta:        
        verbose_name = "Клієнтський контракт (Львів)"
        verbose_name_plural = "Клієнтські контракти (Львів)"
		
    # отримання курсу долара та перерахунок вартості авто на грн.
    def get_commercial_course_usd_test(self):
        #ExchangeRateKyiv.objects.all().filter(date = self.date): # Queryset повертає True, якщо у результаті вибірки є хоча б один елемент
        self.commercial_course_usd_test = ExchangeRateLviv.objects.all().filter(date = self.date)[0].sum if ExchangeRateLviv.objects.all().filter(date = self.date) else 0
        self.initial_cost_car_uah = self.initial_cost_car_usd * self.commercial_course_usd_test
        self.amount_payment_uah = self.amount_payment_usd * self.commercial_course_usd_test
        self.save()
    
    # Розрахунок графіку погашення
    def timetable_calc(self): 
        if self.clientcontracttimetablelviv_set.count() > 0:
            return
        else:
            #today = date.today()
            for i in range(7) :
                day0 = self.date + timedelta(days=i)
                if day0.weekday() == self.frequency_payment:
                    day_1 = day0 if day0 != self.date else  self.date + timedelta(days=7)
                    break
            i = day_1
            day_end = self.date + timedelta(days=self.period_days)
            while i <= day_end:
                #self.clientcontracttimetable_set.create(planned_payment_date = i, planned_amount_payment_usd=self.amount_payment_usd, real_payment_date=i, amount_paid_usd=self.amount_payment_usd)
                self.clientcontracttimetablelviv_set.create(planned_payment_date = i, planned_amount_payment_usd=self.amount_payment_usd, amount_paid_usd=None)
                i = i + timedelta(days=7)
                
    # Розрахунок залишку ТО
    def to_calc(self):
        self.balance_TO_uah = self.clientcontracttolviv_set.all().aggregate(Sum('sum'))['sum__sum']
        self.save()
    
    # Розрахунок номера контракту
    #def number_calc():
    #    return {'number': '200'}
	
    def calc_loan_amount_paid(self):
        """ Розрахунок виплаченої суми кредиту та залишку по кредиту """
    
        today=date.today()
        #self.loan_amount_paid_usd = self.clientcontracttimetable_set.all().filter(real_payment_date__lte=today).aggregate(Sum('amount_paid_usd'))['amount_paid_usd__sum']
        self.loan_amount_paid_usd = self.clientcontracttimetablelviv_set.all().filter(planned_payment_date__lte=today).aggregate(Sum('amount_paid_usd'))['amount_paid_usd__sum'] or 0
        self.loan_amount_to_be_paid_usd = self.initial_cost_car_usd - self.loan_amount_paid_usd
        self.save()
		
# Клієнтський контракт, графік погашення	(тіло + %)	
class ClientContractTimetable(models.Model):
    client_contract = models.ForeignKey(ClientContract, on_delete=models.CASCADE, default=1)								# клієнтський контракт
    planned_payment_date = models.DateTimeField('Дата платежу', null=True, default = timezone.now)													# Планова дата платежу -> Дата платежу
    planned_amount_payment_usd = models.FloatField('Планова сума платежу, в доларах', null=True, blank=True)	# Планова сума платежу, в доларах
    #real_payment_date = models.DateField('Дійсна дата платежу', null=True, blank=True, default = date.today())										# Дійсна дата платежу
    amount_paid_usd = models.FloatField('Оплачена сума, в доларах', null=True, blank=True) 													# Оплачена сума, в доларах
    note = models.CharField('Примітки', max_length=100, null=True, blank = True) 													# Примітки
    # ...
    #def __str__(self):
    #   return self.number
    class Meta:
        abstract = True	
        verbose_name = "Клієнтський контракт, графік погашення"
        verbose_name_plural = "Клієнтський контракт, графік погашення"

    def __str__(self):
        return ""

class ClientContractTimetableKyiv(ClientContractTimetable):
    """ # Клієнтський контракт (Київ), графік погашення	(тіло + %) """
    client_contract = models.ForeignKey(ClientContractKyiv, on_delete=models.CASCADE, default=1)								# клієнтський контракт

class ClientContractTimetableLviv(ClientContractTimetable):
    """ # Клієнтський контракт (Львів), графік погашення	(тіло + %) """
    client_contract = models.ForeignKey(ClientContractLviv, on_delete=models.CASCADE, default=1)								# клієнтський контракт

class ClientContractTO(models.Model):
    """ Клієнтський контракт, ТО (кошти на ТехОбслуговування) """
    client_contract = models.ForeignKey(ClientContract, on_delete=models.CASCADE, default=1)		# клієнтський контракт
    date = models.DateField('Дата платежу (ТО)', null=True, default = date.today)															# Дата платежу (ТО)
    sum = models.FloatField('Сума платежу (ТО)', null=True) 															# Сума платежу (ТО)
    note = models.CharField('Примітки', max_length=100, null=True, blank = True) 							# Примітки
	
    class Meta:
        abstract = True	
        verbose_name = "Клієнтський контракт, ТО"
        verbose_name_plural = "Клієнтський контракт, ТО"

    def __str__(self):
        return ""

class ClientContractTOKyiv(ClientContractTO):
    """ Клієнтський контракт, ТО, Київ (кошти на ТехОбслуговування) """
    client_contract = models.ForeignKey(ClientContractKyiv, on_delete=models.CASCADE, default=1)		# клієнтський контракт	

class ClientContractTOLviv(ClientContractTO):
    """ Клієнтський контракт, ТО, Львів (кошти на ТехОбслуговування) """
    client_contract = models.ForeignKey(ClientContractLviv, on_delete=models.CASCADE, default=1)		# клієнтський контракт	
	
class ClientContractTOTodayKyiv(ClientContractTOKyiv):
    """ Клієнтський контракт, ТО; Proxy-модель для вводу даних (для менеджера) (Київ) """
    class Meta:
        proxy = True
        verbose_name = "Клієнтський контракт, ТО; введення даних"
        verbose_name_plural = "Клієнтський контракт, ТО; введення даних"        

    def __str__(self):
        return ""

class ClientContractTOTodayLviv(ClientContractTOLviv):
    """ Клієнтський контракт, ТО; Proxy-модель для вводу даних (для менеджера) (Львів) """
    class Meta:
        proxy = True
        verbose_name = "Клієнтський контракт, ТО; введення даних"
        verbose_name_plural = "Клієнтський контракт, ТО; введення даних"        

    def __str__(self):
        return ""		

class ClientContractWeeklyCarReportKyiv(ClientContractKyiv):
    """ Проксі-Клас для звіту -Тижневий звіт по авто- """
    class Meta:
        proxy = True
        verbose_name = "Клієнтський контракт, Тижневий звіт по авто"
        verbose_name_plural = "Клієнтські контракти, Тижневий звіт по авто"


		
		
		
# Інвестор
class Investor(models.Model):
    full_name = models.CharField('ПІБ', max_length=50) 									# ПІБ
    phone_number = models.CharField('номер телефону', max_length=15)					# номер телефону
    # ...
    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True			
        verbose_name = "Інвестор"
        verbose_name_plural = "Інвестори"
		
# Інвестор, Київ	
class InvestorKyiv(Investor):  
    def __str__(self):
        return self.full_name								
    class Meta:        
        verbose_name = "Інвестор (Київ)"
        verbose_name_plural = "Інвестори (Київ)"
		
# Інвестор, Львів	
class InvestorLviv(Investor):  
    def __str__(self):
        return self.full_name								
    class Meta:        
        verbose_name = "Інвестор (Львів)"
        verbose_name_plural = "Інвестори (Львів)"
		
# Інвесторський контракт		
class InvestorContract(models.Model):
    number = models.IntegerField('Номер контракту', null = True, default = None) 				# номер контракту
    specification_number = models.IntegerField('Номер специфікації контракту', null = True, default = None) 				# Номер специфікації контракту
    city = models.CharField('Місто, де заключений контракт', max_length=10)	# Назва міста, в якому заключений контракт !!! Доопрацювати вибір зі списку
    date = models.DateField('Дата контракту')									# Дата контракту
    investor = models.ForeignKey(InvestorKyiv, on_delete=models.CASCADE, default=1)			# Інвестор    
    #investor_full_name = models.CharField('ПІБ інвестора',max_length=50)				# ПІБ інвестора	
    director_full_name = models.CharField('ПІБ директора фірми/філіалу фірми',max_length=50)				# ПІБ директора фірми/філіалу фірми
    client_full_name = models.CharField('ПІБ клієнта', max_length=50) 					# ПІБ клієнта
    car = models.OneToOneField(CarKyiv, on_delete=models.CASCADE, default=1)			# 	Авто
    initial_cost_car_usd = models.FloatField('Вартість автомобіля в доларах, на момент складання контракту')# Вартість автомобіля в доларах, на момент складання контракту
    initial_cost_car_uah = models.FloatField('Вартість автомобіля в гривні, на момент складання контракту') # Вартість автомобіля в гривні, на момент складання контракту
    period_days = models.IntegerField('Строк контракту, в днях') 				# Строк контракту, в днях
    #period_years = models.IntegerField('Строк контракту, в роках') 			# Строк контракту, в роках
    #frequency_payment = models.CharField('Періодичність оплати', max_length=10)		# Періодичність оплати
    #amount_payment_usd = models.FloatField('Сума платежу в доларах') 					# Сума платежу в доларах; 17.04.2020 пробував закоментити, видавало помилки при міграції, цікаво чому ???
    number_periods = models.IntegerField('Кількість періодів', default=4) 				# Кількість періодів
    status_body = models.FloatField('Стан розрахунку по тілу кредита. Переплата/прострочка (-)', null=True) 					# Стан розрахунку по тілу кредита. Переплата/прострочка (-)
    іnterest_rate = models.FloatField('Процентна ставка', null=True) 								# Процентна ставка
    last_month_percentage = models.FloatField('Відсотки за попередній місяць', null=True) 								# Відсотки за попередній місяць
    status_percentage = models.FloatField('Стан розрахунку по відсотках кредиту. Прострочка (-)', null=True) 					# Стан розрахунку по відсотках кредиту. Прострочка (-)
    #period_1 = models.DateField('Кінцева дата погашення (період 1)', null=True)																# Період 1, тобто перших пів-року
    #period_1_percentage = models.FloatField('Частина основного боргу, у відсотках (період 1)', default=0) 											# Відсоток на період 1
    #period_2 = models.DateField('Кінцева дата погашення (період 2)', null=True)																# Період 2
    #period_2_percentage = models.FloatField('Частина основного боргу, у відсотках (період 2)', default=0) 											# Відсоток на період 2
    #period_3 = models.DateField('Кінцева дата погашення (період 3)', null=True)																# Період 3
    #period_3_percentage = models.FloatField('Частина основного боргу, у відсотках (період 3)', default=0) 											# Відсоток на період 3
    #period_4 = models.DateField('Кінцева дата погашення (період 4)', null=True)																# Період 4
    #period_4_percentage = models.FloatField('Частина основного боргу, у відсотках (період 4)', default=0) 											# Відсоток на період 4     
	# ...
    def __str__(self):
        return str(self.number)
		
    class Meta:
        abstract = True
        verbose_name = "Інвесторський контракт"
        verbose_name_plural = "Інвесторські контракти"
		
    def bodytimetable_calc(self): 
        #self.investorcontractbodytimetable_set.create(payment_date = self.period_1, payment_percentage = self.period_1_percentage, payment_usd = self.period_1_percentage / 100 * self.initial_cost_car_usd)		
        self.investorcontractbodytimetablekyiv_set.update(payment_usd = payment_percentage / 100 * self.initial_cost_car_usd)		
        #
    #  розрахунок status_body
    def status_body_calc(self):
        today=date.today()
        timetable=self.investorcontractbodytimetablekyiv_set.all()
        #print('timetable.aggregate  = ', timetable.all().aggregate(Sum('payment_usd')) )
        #timetable=self.investorcontractbodytimetable_set.objects.all()
        #kkk = self.investorcontractbodytimetable_set.count()
        #kkk=self.investorcontractbodytimetable_set.count()
        if today <= timetable[0].payment_date:
            self.status_body = self.investorcontractbodypaymentkyiv_set.all().aggregate(Sum('sum'))['sum__sum']            
			#self.refresh_from_db()
			#self.status_body.update(self.investorcontractbodypayment_set.all().aggregate(Sum('sum')))
            #print("self.status_body = ", self.status_body)
        else:
            if today > timetable[self.number_periods-1].payment_date:
                self.status_body = self.investorcontractbodypaymentkyiv_set.all().aggregate(Sum('sum'))['sum__sum'] -  timetable.aggregate(Sum('payment_usd'))['payment_usd__sum']
            else:
                for i in 	range(self.number_periods-1):
                    if timetable[i].payment_date<today<=timetable[i+1].payment_date :
                        break
                # відладка
				#print('i = ', i)
                #print('timetable[i].payment_date = ', timetable[i].payment_date, "type = ", type(timetable[i].payment_date))
                #
				#print ('self.investorcontractbodypayment_set.date = ', self.investorcontractbodypayment_set.date)
                self.status_body = self.investorcontractbodypaymentkyiv_set.all().filter(date__lte=timetable[i].payment_date).aggregate(Sum('sum'))['sum__sum'] -  timetable.filter(payment_date__lte=timetable[i].payment_date).aggregate(Sum('payment_usd'))['payment_usd__sum']
                #self.status_body = self.investorcontractbodypayment_set.all().filter(date<=timetable[i].payment_date).aggregate(Sum('sum'))['sum__sum'] -  timetable.aggregate(Sum('payment_usd'))['payment_usd__sum']
        self.save()
        #
    def control_number_periods(self):
        timetable=self.investorcontractbodytimetablekyiv_set.all()
        if self.investorcontractbodytimetablekyiv_set.count() > self.number_periods:
            #print ('karaul')
            #self.message_user(request, "tttr")
            return False

    # Розрахунок відсотків
    def percentage_calc(self):    
        today=date.today()
        if today.month == self.date.month and today.year == self.date.year: # якщо поточний день та день початку договору знаходяться в одному місяці одного року, то нарахування % за минулий місяць, та стан нарахування %  рівні 0
            self.last_month_percentage = 0
            self.status_percentage = 0
        else:
            last_month_last_day = today.replace(day=1) - timedelta(days=1) #останній день останнього місяця
            print('last_month_last_day = ', last_month_last_day, ' number = ', last_month_last_day.day)
            last_month_last_day_body_payments = self.investorcontractbodypaymentkyiv_set.all().filter(date__lte=last_month_last_day)  # платежі по тілу до останнього дня останнього місяця
            last_month_last_day_body_payments_count = last_month_last_day_body_payments.count() # кількість платежів по тілу до останнього дня останнього місяця
            print('last_month_last_day_body_payments_count = ', last_month_last_day_body_payments_count)
            
            #розрахунок кількості днів в останньому місяці
            if last_month_last_day.year == self.date.year and last_month_last_day.month == self.date.month: #якщо контракт почався в минулому місяці
                last_month_days_number = last_month_last_day.day - self.date.day
            else:
                last_month_days_number = last_month_last_day.day
            print('last_month_days_number = ', last_month_days_number)            
            """ # тимчасово закрив, наче зробив універсальний алгоритм, можна врахувати, якщо платежів не було взагалі
            if last_month_last_day_body_payments_count == 0: #якщо платежів по тілу не було взагалі
                self.last_month_percentage = self.initial_cost_car_usd * coef * last_month_days_number # % за останній місяць
                total_calc_percentage = self.initial_cost_car_usd * coef * (last_month_last_day - self.date).days # нараховані % за весь час               
                total_paid_percentage = self.investorcontractpercentagepayment_set.all().filter(date__lte=today).aggregate(Sum('sum'))['sum__sum'] # сплачені % за весь час ; 
                if total_paid_percentage == None:
                    total_paid_percentage = 0
                print('last_month_percentage = ', self.last_month_percentage, ' ; total_calc_percentage = ', total_calc_percentage, ' ; total_paid_percentage = ', total_paid_percentage)
                if today.day > 10: # доперевіряти цю гілку
                   self.status_percentage = total_paid_percentage - total_calc_percentage - self.last_month_percentage
                else:
                   self.status_percentage = total_paid_percentage - total_calc_percentage + self.last_month_percentage
            else:
			"""
            credit_body = self.initial_cost_car_usd # залишок по тілу кредиту, для розрахунку %
            last_payment_date_body = self.date # остання платіжна дата по тілу кредиту
            total_calc_percentage = 0 # нараховані % за весь час               
            self.last_month_percentage = 0 # % за останній місяць
            last_month_body_payments_count = 0 # к-сть платежів по тілу в останньому місяці
            coef = self.іnterest_rate / 100 / 365 # коефіцієнт, щоб не перераховувати його кожен раз 
            # пройтись по всіх  платежах по тілу; і врахувати період від останнього платежу по тілу до кінця місяця !
            for i in range(last_month_last_day_body_payments_count):                               
                total_calc_percentage += credit_body * coef * (last_month_last_day_body_payments[i].date - last_payment_date_body).days # нараховані % за весь час
                # якщо платіж зроблений в останній місяць
                if last_month_last_day.year == last_month_last_day_body_payments[i].date.year and last_month_last_day.month == last_month_last_day_body_payments[i].date.month: 
                    if last_month_body_payments_count == 0: # якщо це перший платіж в останньому місяці, то різницю днів обраховуємо від першого дня чи початку контракту, інакше - від попереднього платежу
                        if last_month_days_number != last_month_last_day.day: # контракт почався в останній місяць
                            days_number =  last_month_last_day_body_payments[i].date - self.date
                        else:
                            days_number = last_month_last_day_body_payments[i].date - last_month_last_day.replace(day=1)
                        last_month_body_payments_count = 1
                        #print('last_month_last_day.replace(day=1) = ', last_month_last_day.replace(day=1), ' last_month_last_day_body_payments[i].date = ', last_month_last_day_body_payments[i].date, ' days_number = ', days_number )
                    else:
                        days_number = last_month_last_day_body_payments[i].date - last_month_last_day_body_payments[i-1].date
                    self.last_month_percentage += credit_body * coef * days_number.days
                credit_body -= last_month_last_day_body_payments[i].sum
                last_payment_date_body = last_month_last_day_body_payments[i].date
                print ('total_calc_percentage = ', total_calc_percentage, ' credit_body = ', credit_body,  ' last_payment_date_body = ', last_payment_date_body, ' self.last_month_percentage = ', self.last_month_percentage)   
            if last_payment_date_body == last_month_last_day: # якщо останній платіж відбувся в останній день місяця, то більше нічого робити не потрібно
                pass
            else:
                # донарахувати відсотки загальні та за останній місяць; вивести різницю між сплаченими та нарахованими; врахувати 10-те число                    
                total_calc_percentage += credit_body * coef * (last_month_last_day - last_payment_date_body).days # нараховані % за весь час
                if last_month_body_payments_count > 0:
                    self.last_month_percentage += credit_body * coef * (last_month_last_day - last_payment_date_body).days
                else:
                    self.last_month_percentage = credit_body * coef * last_month_days_number # % за останній місяць
            total_paid_percentage = self.investorcontractpercentagepaymentkyiv_set.all().filter(date__lte=today).aggregate(Sum('sum'))['sum__sum'] # сплачені % за весь час ;
            if total_paid_percentage == None:
                total_paid_percentage = 0
            print('last_month_percentage = ', self.last_month_percentage, ' ; total_calc_percentage = ', total_calc_percentage, ' ; total_paid_percentage = ', total_paid_percentage)
            if today.day > 10: # доперевіряти цю гілку
               self.status_percentage = format(total_paid_percentage - total_calc_percentage, '.2f')
            else:
               self.status_percentage = format(total_paid_percentage - total_calc_percentage + self.last_month_percentage, '.2f')
                #self.last_month_percentage += credit_body * coef * (last_month_last_day - last_payment_date_body).days # ??? Якщо платіж не в останньому місяці ?
                #total_calc_percentage +=                     
        self.save()

class InvestorContractKyiv(InvestorContract):

    class Meta:        
        verbose_name = "Інвесторський контракт (Київ)"
        verbose_name_plural = "Інвесторські контракти (Київ)"


class InvestorContractLviv(InvestorContract):
    investor = models.ForeignKey(InvestorLviv, on_delete=models.CASCADE, default=1)			# Інвестор 
    car = models.OneToOneField(CarLviv, on_delete=models.CASCADE, default=1)			# 	Авто	

    class Meta:        
        verbose_name = "Інвесторський контракт (Львів)"
        verbose_name_plural = "Інвесторські контракти (Львів)"

    def bodytimetable_calc(self): 
        #self.investorcontractbodytimetable_set.create(payment_date = self.period_1, payment_percentage = self.period_1_percentage, payment_usd = self.period_1_percentage / 100 * self.initial_cost_car_usd)		
        self.investorcontractbodytimetablelviv_set.update(payment_usd = payment_percentage / 100 * self.initial_cost_car_usd)		
        #
    #  розрахунок status_body
    def status_body_calc(self):
        today=date.today()
        timetable=self.investorcontractbodytimetablelviv_set.all()
        #print('timetable.aggregate  = ', timetable.all().aggregate(Sum('payment_usd')) )
        #timetable=self.investorcontractbodytimetable_set.objects.all()
        #kkk = self.investorcontractbodytimetable_set.count()
        #kkk=self.investorcontractbodytimetable_set.count()
        if today <= timetable[0].payment_date:
            self.status_body = self.investorcontractbodypaymentlviv_set.all().aggregate(Sum('sum'))['sum__sum']            
			#self.refresh_from_db()
			#self.status_body.update(self.investorcontractbodypayment_set.all().aggregate(Sum('sum')))
            #print("self.status_body = ", self.status_body)
        else:
            if today > timetable[self.number_periods-1].payment_date:
                self.status_body = self.investorcontractbodypaymentlviv_set.all().aggregate(Sum('sum'))['sum__sum'] -  timetable.aggregate(Sum('payment_usd'))['payment_usd__sum']
            else:
                for i in 	range(self.number_periods-1):
                    if timetable[i].payment_date<today<=timetable[i+1].payment_date :
                        break
                # відладка
				#print('i = ', i)
                #print('timetable[i].payment_date = ', timetable[i].payment_date, "type = ", type(timetable[i].payment_date))
                #
				#print ('self.investorcontractbodypayment_set.date = ', self.investorcontractbodypayment_set.date)
                self.status_body = self.investorcontractbodypaymentlviv_set.all().filter(date__lte=timetable[i].payment_date).aggregate(Sum('sum'))['sum__sum'] -  timetable.filter(payment_date__lte=timetable[i].payment_date).aggregate(Sum('payment_usd'))['payment_usd__sum']
                #self.status_body = self.investorcontractbodypayment_set.all().filter(date<=timetable[i].payment_date).aggregate(Sum('sum'))['sum__sum'] -  timetable.aggregate(Sum('payment_usd'))['payment_usd__sum']
        self.save()
        #
    def control_number_periods(self):
        timetable=self.investorcontractbodytimetablelviv_set.all()
        if self.investorcontractbodytimetablelviv_set.count() > self.number_periods:
            #print ('karaul')
            #self.message_user(request, "tttr")
            return False

    # Розрахунок відсотків
    def percentage_calc(self):    
        today=date.today()
        if today.month == self.date.month and today.year == self.date.year: # якщо поточний день та день початку договору знаходяться в одному місяці одного року, то нарахування % за минулий місяць, та стан нарахування %  рівні 0
            self.last_month_percentage = 0
            self.status_percentage = 0
        else:
            last_month_last_day = today.replace(day=1) - timedelta(days=1) #останній день останнього місяця
            print('last_month_last_day = ', last_month_last_day, ' number = ', last_month_last_day.day)
            last_month_last_day_body_payments = self.investorcontractbodypaymentlviv_set.all().filter(date__lte=last_month_last_day)  # платежі по тілу до останнього дня останнього місяця
            last_month_last_day_body_payments_count = last_month_last_day_body_payments.count() # кількість платежів по тілу до останнього дня останнього місяця
            print('last_month_last_day_body_payments_count = ', last_month_last_day_body_payments_count)
            
            #розрахунок кількості днів в останньому місяці
            if last_month_last_day.year == self.date.year and last_month_last_day.month == self.date.month: #якщо контракт почався в минулому місяці
                last_month_days_number = last_month_last_day.day - self.date.day
            else:
                last_month_days_number = last_month_last_day.day
            print('last_month_days_number = ', last_month_days_number)            
            """ # тимчасово закрив, наче зробив універсальний алгоритм, можна врахувати, якщо платежів не було взагалі
            if last_month_last_day_body_payments_count == 0: #якщо платежів по тілу не було взагалі
                self.last_month_percentage = self.initial_cost_car_usd * coef * last_month_days_number # % за останній місяць
                total_calc_percentage = self.initial_cost_car_usd * coef * (last_month_last_day - self.date).days # нараховані % за весь час               
                total_paid_percentage = self.investorcontractpercentagepayment_set.all().filter(date__lte=today).aggregate(Sum('sum'))['sum__sum'] # сплачені % за весь час ; 
                if total_paid_percentage == None:
                    total_paid_percentage = 0
                print('last_month_percentage = ', self.last_month_percentage, ' ; total_calc_percentage = ', total_calc_percentage, ' ; total_paid_percentage = ', total_paid_percentage)
                if today.day > 10: # доперевіряти цю гілку
                   self.status_percentage = total_paid_percentage - total_calc_percentage - self.last_month_percentage
                else:
                   self.status_percentage = total_paid_percentage - total_calc_percentage + self.last_month_percentage
            else:
			"""
            credit_body = self.initial_cost_car_usd # залишок по тілу кредиту, для розрахунку %
            last_payment_date_body = self.date # остання платіжна дата по тілу кредиту
            total_calc_percentage = 0 # нараховані % за весь час               
            self.last_month_percentage = 0 # % за останній місяць
            last_month_body_payments_count = 0 # к-сть платежів по тілу в останньому місяці
            coef = self.іnterest_rate / 100 / 365 # коефіцієнт, щоб не перераховувати його кожен раз 
            # пройтись по всіх  платежах по тілу; і врахувати період від останнього платежу по тілу до кінця місяця !
            for i in range(last_month_last_day_body_payments_count):                               
                total_calc_percentage += credit_body * coef * (last_month_last_day_body_payments[i].date - last_payment_date_body).days # нараховані % за весь час
                # якщо платіж зроблений в останній місяць
                if last_month_last_day.year == last_month_last_day_body_payments[i].date.year and last_month_last_day.month == last_month_last_day_body_payments[i].date.month: 
                    if last_month_body_payments_count == 0: # якщо це перший платіж в останньому місяці, то різницю днів обраховуємо від першого дня чи початку контракту, інакше - від попереднього платежу
                        if last_month_days_number != last_month_last_day.day: # контракт почався в останній місяць
                            days_number =  last_month_last_day_body_payments[i].date - self.date
                        else:
                            days_number = last_month_last_day_body_payments[i].date - last_month_last_day.replace(day=1)
                        last_month_body_payments_count = 1
                        #print('last_month_last_day.replace(day=1) = ', last_month_last_day.replace(day=1), ' last_month_last_day_body_payments[i].date = ', last_month_last_day_body_payments[i].date, ' days_number = ', days_number )
                    else:
                        days_number = last_month_last_day_body_payments[i].date - last_month_last_day_body_payments[i-1].date
                    self.last_month_percentage += credit_body * coef * days_number.days
                credit_body -= last_month_last_day_body_payments[i].sum
                last_payment_date_body = last_month_last_day_body_payments[i].date
                print ('total_calc_percentage = ', total_calc_percentage, ' credit_body = ', credit_body,  ' last_payment_date_body = ', last_payment_date_body, ' self.last_month_percentage = ', self.last_month_percentage)   
            if last_payment_date_body == last_month_last_day: # якщо останній платіж відбувся в останній день місяця, то більше нічого робити не потрібно
                pass
            else:
                # донарахувати відсотки загальні та за останній місяць; вивести різницю між сплаченими та нарахованими; врахувати 10-те число                    
                total_calc_percentage += credit_body * coef * (last_month_last_day - last_payment_date_body).days # нараховані % за весь час
                if last_month_body_payments_count > 0:
                    self.last_month_percentage += credit_body * coef * (last_month_last_day - last_payment_date_body).days
                else:
                    self.last_month_percentage = credit_body * coef * last_month_days_number # % за останній місяць
            total_paid_percentage = self.investorcontractpercentagepaymentlviv_set.all().filter(date__lte=today).aggregate(Sum('sum'))['sum__sum'] # сплачені % за весь час ;
            if total_paid_percentage == None:
                total_paid_percentage = 0
            print('last_month_percentage = ', self.last_month_percentage, ' ; total_calc_percentage = ', total_calc_percentage, ' ; total_paid_percentage = ', total_paid_percentage)
            if today.day > 10: # доперевіряти цю гілку
               self.status_percentage = format(total_paid_percentage - total_calc_percentage, '.2f')
            else:
               self.status_percentage = format(total_paid_percentage - total_calc_percentage + self.last_month_percentage, '.2f')
                #self.last_month_percentage += credit_body * coef * (last_month_last_day - last_payment_date_body).days # ??? Якщо платіж не в останньому місяці ?
                #total_calc_percentage +=                     
        self.save()
		
# Інвесторський контракт, графік погашення	тіла кредиту		
# Це саме графік погашення тіла, платежі будуть винесені в окрему таблицю
class InvestorContractBodyTimetable(models.Model):
    investor_contract = models.ForeignKey(InvestorContractKyiv, on_delete=models.CASCADE, default=1)		# інвесторський контракт
    payment_date = models.DateField('Планова кінцева дата погашення', null=True)																# Період 1, тобто перших пів-року
    payment_percentage = models.FloatField('Частина основного боргу, у відсотках', default=0) 	
    payment_usd = models.FloatField('Частина основного боргу, у доларах', default = 0) 	    
    #real_payment_date = models.DateField('Дійсна дата платежу', null=True)									# Дійсна дата платежу
    #amount_paid_usd = models.FloatField('Оплачена сума, в доларах', null=True) 											# Оплачена сума, в доларах
    # ...
    #def __str__(self):
    #   return self.number
    class Meta:
        abstract = True
        ordering = ['payment_date']
        verbose_name = "Інвесторський контракт, графік погашення	тіла кредиту"
        verbose_name_plural = "Інвесторський контракт, графік погашення тіла кредиту"
		
class InvestorContractBodyTimetableKyiv(InvestorContractBodyTimetable):
    
    pass


class InvestorContractBodyTimetableLviv(InvestorContractBodyTimetable):    
    investor_contract = models.ForeignKey(InvestorContractLviv, on_delete=models.CASCADE, default=1)		# інвесторський контракт
	
	
# Інвесторський контракт, платежі по тілу кредиту
class InvestorContractBodyPayment(models.Model):
    investor_contract = models.ForeignKey(InvestorContractKyiv, on_delete=models.CASCADE, default=1)		# інвесторський контракт
    date = models.DateField('Дата платежу', null=True)																# Дата платежу
    sum = models.FloatField('Сума платежу (погашення тіла боргу)', default=0) 							# Сума платежу (погашення тіла боргу)
	
    class Meta:
        abstract = True	
        verbose_name = "Інвесторський контракт, платежі по тілу кредиту"
        verbose_name_plural = "Інвесторський контракт, платежі по тілу кредиту"
		
class InvestorContractBodyPaymentKyiv(InvestorContractBodyPayment):
    pass

class InvestorContractBodyPaymentLviv(InvestorContractBodyPayment):
    investor_contract = models.ForeignKey(InvestorContractLviv, on_delete=models.CASCADE, default=1)		# інвесторський контракт
	
# Інвесторський контракт, платежі по % на тіло кредиту !!! змінити назву полів
class InvestorContractPercentagePayment(models.Model):
    investor_contract = models.ForeignKey(InvestorContractKyiv, on_delete=models.CASCADE, default=1)		# інвесторський контракт
    #planned_payment_date = models.DateField('Планова дата платежу', null=True)							# Планова дата платежу
    #planned_amount_payment_usd = models.FloatField('Планова сума платежу, в доларах', null=True)							# Планова сума платежу, в доларах
    date = models.DateField('Дійсна дата платежу', null=True)									# Дійсна дата платежу
    sum = models.FloatField('Оплачена сума, в доларах', null=True) 											# Оплачена сума, в доларах
    # ...
    #def __str__(self):
    #   return self.number
    class Meta:
        abstract = True
        verbose_name = "Інвесторський контракт, платежі по % на тіло кредиту"
        verbose_name_plural = "Інвесторський контракт, платежі по % на тіло кредиту"
		
class InvestorContractPercentagePaymentKyiv(InvestorContractPercentagePayment):
    pass
	
class InvestorContractPercentagePaymentLviv(InvestorContractPercentagePayment):
    investor_contract = models.ForeignKey(InvestorContractLviv, on_delete=models.CASCADE, default=1)		# інвесторський контракт
	
	
	
#class YourModel(models.Model):
#    pass
    
    
#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

