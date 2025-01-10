from django.shortcuts import render
from django.http import HttpResponse
from online_store.models import Product, Category


def home(request):
    products = Product.objects.all
    context = {
        'products': products,
    }
    return render(request, 'online_store/home.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("message")
        print(f"Имя - {name}\nПочта - {email}\nСообщение - {massage}")
        return HttpResponse(f"Спасибо {name}!")

    return render(request, 'online_store/contacts.html')

def categories(request):
    сategorys = Category.objects.all
    context = {
        'сategorys': сategorys,
    }
    return render(request, 'online_store/categories.html',context)

def orders(request):
    return render(request, 'online_store/orders.html')

def pattern(request):
    return render(request, 'online_store/pattern.html')
def index(request):
    product = Product.objects.get(id=9)
    context = {
        'product': product,
        'name': product.name,
        'description': product.description,
        'preview': product.preview,
    }
    return render(request, 'online_store/index.html', context)