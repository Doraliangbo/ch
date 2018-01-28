from django.contrib import admin
from .models import City, Menu, MenuItem, MenuSection, Resturant, StateOrProvince

# Register your models here.

class MenuItemInline(admin.TabularInline):
    model = MenuItem

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

admin.site.register(City)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem)
admin.site.register(MenuSection)
admin.site.register(Resturant)
admin.site.register(StateOrProvince)