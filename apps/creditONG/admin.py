from django.contrib import admin
from .models import Credit, Item

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
