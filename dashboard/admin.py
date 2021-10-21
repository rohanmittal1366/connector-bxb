from django.contrib import admin
from .models import Product

# Register your models here.
# declare here and it will access the product and show it to you on admin panel
admin.site.register(Product)