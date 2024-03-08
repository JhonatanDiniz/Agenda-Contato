from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'created_date', 'show')
    list_display_links=('id', 'first_name',)
    search_fields=('first_name', 'last_name',)
    list_editable=('show',)
    list_per_page=10
    ordering=('-id',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
    list_display_links=('id', 'name')
