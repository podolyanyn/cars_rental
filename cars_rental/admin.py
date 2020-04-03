from django.contrib import admin

# Register your models here.
from .models import Client, Investor, Car, ClientContract, InvestorContract, Color
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
admin.site.register(Car)
#admin.site.register(CarOdesa)
admin.site.register(ClientContract)
#admin.site.register(ClientContractOdesa)
admin.site.register(InvestorContract)
#admin.site.register(InvestorContractOdesa)
admin.site.register(Color)