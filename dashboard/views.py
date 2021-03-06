from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # for give permision according to the user and admin
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User # for give permision according to the user and admin
from django.contrib import messages
from .filters import StaffFilter, ProductFilter,OrderFilter
from django.db.models import Max
# Create your views here.

@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    product  = Product.objects.all()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # we need an instance bcz we want to save user name for making request
            instance =  form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders' : orders,
        'form' : form,
        'products' : product,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'product_count': product_count
    } 
    return render(request, "dashboard/index.html" , context)
    # return HttpResponse('This is index page')

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    myFilter = StaffFilter(request.GET, queryset = workers)
    workers = myFilter.qs

    context = {
        'workers': workers,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'product_count': product_count,
        'myFilter' : myFilter,
    }
    return render(request, "dashboard/staff.html", context)

@login_required(login_url='user-login')
def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    
    context = {
        'worker': worker,
        
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all() # using  object relational mapping 
    # items = Product.objects.raw('SELECT * FROM dashboard_product')
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    myFilter_product = ProductFilter(request.GET, queryset = items)
    items = myFilter_product.qs

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')

    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' : form,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'product_count': product_count,
        'myFilter_product' : myFilter_product,
    }
    return render(request, "dashboard/product.html", context)

@login_required(login_url='user-login')
def product_delete(request , pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    myFilter_order = OrderFilter(request.GET, queryset = orders)
    orders = myFilter_order.qs
    myFilter_order = OrderFilter(request.GET, queryset = orders) 

    # min1=0
    # max1=0
    # if 'min_order_quantity' in request.GET:
    #     min1 = request.GET.get('min_order_quantity')
    #     max1 = request.GET.get('max_order_quantity')
    #     if min1 == '':
    #         min1 = 0
    #     if max1 == '':
    #         max1= orders.aggregate(Max('order_quantity'))

    # myFilter_range = Order.objects.filter(quantity__range=(min1,max1)) 

    context = {
        'orders': orders,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'product_count': product_count,
        'myFilter_order' : myFilter_order,
        # 'myFilter_range': myFilter_range,

    }
    return render(request, "dashboard/order.html", context)


#   if 'min_price' in request.GET:
#         filter_price1 = request.GET.get('min_price')
#         filter_price2 = request.GET.get('max_price')
#         if filter_price1 =='':
#             filter_price1=0
#         if filter_price2=='':
#             filter_price2=Add_prod.objects.all().aggregate(Max('price'))
#         my_products = Add_prod.objects.filter(price__range=(filter_price1,filter_price2))