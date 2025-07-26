from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza,Pasta

# Create your views here.
# /menu
def index(request):
    pizzas=Pizza.objects.all().order_by('price')
    # pizzas_names_and_price = [pizza.name + " : " + str(pizza.price) + " ₹" for pizza in pizzas]
    # pizzas_names_and_price_str=", ".join(pizzas_names_and_price)
    # return HttpResponse("Our Pizzas : " + pizzas_names_and_price_str)
    return render(request, 'menu/index.html', {'pizzas' : pizzas})

def pasta(request):
    pastas=Pasta.objects.all().order_by('price')
    return render(request, 'menu/pasta.html', {'pastas' : pastas})