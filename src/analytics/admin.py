from django.contrib import admin

# Register your models here.

from .models import ClickEvent

admin.site.register(ClickEvent)