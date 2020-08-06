from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AboutMe)
admin.site.register(TimeLine)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone','email', 'status']
    list_editable = ['status']
    list_filter = ['status']
    search_fields = ('name', 'phone')
    readonly_fields =('name', 'phone', 'email', 'message')

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name', 'description']
