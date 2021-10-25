from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # for give permision according to the user and admin
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User # for give permision according to the user and admin
from django.contrib import messages
# Create your views here.

@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    product  = Product.objects.all()
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
        'products' : product
    } 
    return render(request, "dashboard/index.html" , context)
    # return HttpResponse('This is index page')

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    context = {
        'workers': workers
    }
    return render(request, "dashboard/staff.html", context)

@login_required(login_url='user-login')
def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    context = {
        'worker': worker
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all() # using  object relational mapping 
    # items = Product.objects.raw('SELECT * FROM dashboard_product')
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
    context = {
        'orders': orders
    }
    return render(request, "dashboard/order.html", context)

