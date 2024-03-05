from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'created_date')
    list_display_links=('id', 'first_name',)
    search_fields=('first_name', 'last_name',)
    ordering=('id',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
    list_display_links=('id', 'name')
