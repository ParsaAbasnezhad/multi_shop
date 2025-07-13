from django.contrib import admin
from .models import ShopDetail
from .models import Size
from .models import Color

admin.site.register(Size)
admin.site.register(Color)


@admin.register(ShopDetail)
class ShopListAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_filter = ('status',)
    search_fields = ('title',)
