# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from webportal.models import Support, Module

admin.site.register(Support)
admin.site.register(Module)
