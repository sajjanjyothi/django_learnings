# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Publisher

# Register your models here.
# class PublisherAdmin(admin.ModelAdmin):
# 	pass


admin.site.register(Publisher)
