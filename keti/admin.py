from django.contrib import admin
from .models import AiriotTable
from .models import AirqualityTable
from .models import SmartthingsTable
from .models import UvTable
from .models import WayskinTable
from .models import WeatherTable
from .models import UserTable

# Register your models here.


admin.site.register(AiriotTable)
admin.site.register(AirqualityTable)
admin.site.register(SmartthingsTable)
admin.site.register(UvTable)
admin.site.register(WayskinTable)
admin.site.register(WeatherTable)
admin.site.register(UserTable)
