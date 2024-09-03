from django.contrib import admin
from .models import Menu, Log, MenuGenre

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuGenre)
admin.site.register(Log)