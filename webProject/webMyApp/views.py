from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Product


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, 'login.html', {'error': 'Nieprawidłowe dane do logowania'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'display.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        
        new_product = Product(name=name, category=category, price=price)
        new_product.save()
        return redirect('product_list')
    return render(request, 'index.html')