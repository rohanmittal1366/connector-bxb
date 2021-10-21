from django.contrib import admin
from .models import Product , Order
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'Connector BxB'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' ,'category', 'quantity')
    list_filter = ['category'] # it filter the content by category in admin panel


# declare here and it will access the product and show it to you on admin panel
admin.site.register(Product , ProductAdmin)
admin.site.register(Order )
# admin.site.unregister(Group) 