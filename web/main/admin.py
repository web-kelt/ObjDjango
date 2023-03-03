from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Object


@admin.register(Object)
class News_admin(ModelAdmin):
    pass
