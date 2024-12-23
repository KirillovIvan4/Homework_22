from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'online_store/home.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("message")
        print(f"Имя - {name}\nПочта - {email}\nСообщение - {massage}")
        return HttpResponse(f"Спасибо {name}!")

    return render(request, 'online_store/contacts.html')

def categories(request):
    return render(request, 'online_store/categories.html')

def orders(request):
    return render(request, 'online_store/orders.html')