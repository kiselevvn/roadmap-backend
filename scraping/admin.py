from django.contrib import admin
from django.contrib.admin import (ModelAdmin, StackedInline, TabularInline,
                                  register)

from .models import Response, Site


@register(Site)
class SiteAdmin(ModelAdmin):
    pass


@register(Response)
class ResponseAdmin(ModelAdmin):
    pass