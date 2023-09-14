from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre',)
