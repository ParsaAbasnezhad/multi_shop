from django.contrib import admin
from .models import Detail
from .models import Size
from .models import Color
from .models import Information

admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Information)


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_filter = ('status',)
    search_fields = ('title',)
