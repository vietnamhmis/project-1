from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

admin.site.register(Item1)

admin.site.register(Order1)

admin.site.register(OrderItem1)

admin.site.register(Billingaddress1)

class OrderItem1(admin.ModelAdmin):
    OrderItem1 = ('id', 'Chi_tieu', 'Ket_qua')
