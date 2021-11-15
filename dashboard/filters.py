import django_filters

from .models import *

class StaffFilter(django_filters.FilterSet):
    class  Meta:
        model = User
        fields = ['username',]



class ProductFilter(django_filters.FilterSet):
    class  Meta:
        model = Product
        fields = '__all__'


class OrderFilter(django_filters.FilterSet):
    class  Meta:
        model = Order
        fields = ['product','product__category','staff']

