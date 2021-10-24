from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # for give permision according to the user and admin
from .models import Product
from .forms import ProductForm
# Create your views here.

@login_required(login_url='user-login')
def index(request):
    return render(request, "dashboard/index.html")
    # return HttpResponse('This is index page')

@login_required(login_url='user-login')
def staff(request):
    return render(request, "dashboard/staff.html")

@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all() # using  object relational mapping 
    # items = Product.objects.raw('SELECT * FROM dashboard_product')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
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
def order(request):
    return render(request, "dashboard/order.html")

