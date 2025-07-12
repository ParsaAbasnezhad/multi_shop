from django.contrib import admin
from .models import ShopList




@admin.register(ShopList)
class ShopListAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('status',)
    search_fields = ('name',)
