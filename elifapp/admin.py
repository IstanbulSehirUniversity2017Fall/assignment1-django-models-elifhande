# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Series
from.models import Episode
# Register your models here.
admin.site.register(Series)
admin.site.register(Episode)