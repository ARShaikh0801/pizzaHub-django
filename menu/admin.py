from django.contrib import admin
from .models import Pizza,Pasta

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name','ingredients','vegetarian','price')
    search_fields=['name']
    
class PastaAdmin(admin.ModelAdmin):
    list_display = ('name','ingredients','vegetarian','price')
    search_fields=['name']

# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pasta, PastaAdmin)