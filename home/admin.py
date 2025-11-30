# admin.py
from django.contrib import admin
from .models import LeadModel

@admin.register(LeadModel)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'get_consultation_types_display', 'created_at')
    list_filter = ('consultation_types', 'created_at')
    search_fields = ('name', 'email', 'phone')

    list_display_links = ('name',)