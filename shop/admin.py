from django.contrib import admin
from .models import Detail
from .models import Size
from .models import Color

admin.site.register(Size)
admin.site.register(Color)


@admin.register(Detail)
class ShopListAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_filter = ('status',)
    search_fields = ('title',)
