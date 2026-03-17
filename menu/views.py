from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Pizza, Pasta


def index(request):
    pizzas=Pizza.objects.all().order_by('price')
    # pizzas_names_and_price = [pizza.name + " : " + str(pizza.price) + " ₹" for pizza in pizzas]
    # pizzas_names_and_price_str=", ".join(pizzas_names_and_price)
    # return HttpResponse("Our Pizzas : " + pizzas_names_and_price_str)
    return render(request, 'menu/index.html', {'pizzas' : pizzas})

def pasta(request):
    """Display all pastas sorted by price."""
    pastas = Pasta.objects.all().order_by('price')
    return render(request, 'menu/pasta.html', {'pastas': pastas})


def api_get_pizzas(request):
    """Return all pizzas and pastas as JSON."""
    pizzas = Pizza.objects.all().order_by('price')
    pastas = Pasta.objects.all().order_by('price')
    pizzas_json = serializers.serialize("json", pizzas)
    pastas_json = serializers.serialize("json", pastas)
    return HttpResponse([pizzas_json, pastas_json])