from django.contrib import admin
from django.contrib.admin import (ModelAdmin, StackedInline, TabularInline,
                                  register)

from .models import Block, Roadmap, SiteParam


class BlockInline(StackedInline):
    extra = 0
    model = Block


@register(Roadmap)
class RoadmapAdmin(ModelAdmin):
    inlines = [BlockInline]




class SiteParamInline(StackedInline):
    extra = 0
    model = SiteParam

@register(Block)
class BlockAdmin(ModelAdmin):
    inlines = [SiteParamInline]