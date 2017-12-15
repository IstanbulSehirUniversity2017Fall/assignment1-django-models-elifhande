# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.test import TestCase


def index(request):
    return HttpResponse("<h1>Hi!<h1>")


def series_details(request, series_number):
    return HttpResponse("<h2>This is series number %s<h2>"%str(series_number))


class SeriesViewsTest(TestCase):
    def test_index(self):
        response = self.client.get(reversed('index'))
        self.assertEqual(response.status_code, 200)