from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ShopUnit)
admin.site.register(ShopUnitImport)
admin.site.register(ShopUnitImportRequest)
admin.site.register(ShopUnitStatisticUnit)
admin.site.register(ShopUnitStatisticResponse)
admin.site.register(Error)
