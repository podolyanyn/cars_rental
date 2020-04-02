from django.db import models

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
		
# Авто
class Car(models.Model):
    brand = models.CharField('Марка', max_length=20) 									# марка
    model = models.CharField('Модель', max_length=20)									# модель
    production_year = models.IntegerField('Рік випуску')								# рік  випуску
    car_body_number = models.CharField('Номер кузова', max_length=30)					# номер кузова
    license_plate = models.CharField('Номерний знак', max_length=30)					# номерний знак
    car_color = models.CharField('Колір', max_length=30, null=True)						# Колір
    car_mileage = models.IntegerField('Пробіг', null=True)											# Пробіг
    # ...
    def __str__(self):
        return self.car_body_number
		
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
    contract_number = models.CharField('Номер контракту', max_length=10) 				# номер контракту
    contract_city = models.CharField('Місто, де заключений контракт', max_length=10)	# Назва міста, в якому заключений контракт !!! Доопрацювати вибір зі списку
    contract_date = models.DateField('Дата контракту')									# Дата контракту
    investor_full_name = models.CharField('ПІБ інвестора',max_length=50)				# ПІБ інвестора	
    director_full_name = models.CharField('ПІБ директора фірми/філіалу фірми',max_length=50)				# ПІБ директора фірми/філіалу фірми
    client_full_name = models.CharField('ПІБ клієнта', max_length=50) 					# ПІБ клієнта
    initial_cost_car_usd = models.FloatField('Вартість автомобіля в доларах, на момент складання контракту')# Вартість автомобіля в доларах, на момент складання контракту
    commercial_course_usd = models.FloatField('Комерційний курс долара', null=True)		# Комерційний курс долара
    initial_cost_car_uah = models.FloatField('Вартість автомобіля в гривні, на момент складання контракту') # Вартість автомобіля в гривні, на момент складання контракту; автоматичний перерахунок, поле не редагується
    contract_period_days = models.IntegerField('Строк контракту, в днях') 				# Строк контракту, в днях
    #contract_period_years = models.IntegerField('Строк контракту, в роках') 			# Строк контракту, в роках
    frequency_payment = models.CharField('Періодичність оплати', max_length=10)			# Періодичність оплати
    amount_payment_usd = models.FloatField('Сума платежу в доларах') 					# Сума платежу в доларах    
    amount_payment_uah = models.FloatField('Сума платежу в гривнях', null=True)			# Сума платежу в гривнях; автоматичний перерахунок, поле не редагується	
    # ...
    def __str__(self):
        return self.contract_number
		
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
    investor_full_name = models.CharField('ПІБ інвестора',max_length=50)				# ПІБ інвестора	
    director_full_name = models.CharField('ПІБ директора фірми/філіалу фірми',max_length=50)				# ПІБ директора фірми/філіалу фірми
    client_full_name = models.CharField('ПІБ клієнта', max_length=50) 					# ПІБ клієнта
    initial_cost_car_usd = models.FloatField('Вартість автомобіля в доларах, на момент складання контракту')# Вартість автомобіля в доларах, на момент складання контракту
    initial_cost_car_uah = models.FloatField('Вартість автомобіля в гривні, на момент складання контракту') # Вартість автомобіля в гривні, на момент складання контракту
    contract_period_days = models.IntegerField('Строк контракту, в днях') 				# Строк контракту, в днях
    #contract_period_years = models.IntegerField('Строк контракту, в роках') 			# Строк контракту, в роках
    #frequency_payment = models.CharField('Періодичність оплати', max_length=10)		# Періодичність оплати
    #amount_payment_usd = models.FloatField('Сума платежу в доларах') 					# Сума платежу в доларах
    іnterest_rate = models.FloatField('Процентна ставка', null=True) 								# Процентна ставка
	# ...
    def __str__(self):
        return self.contract_number
		
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