# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Series(models.Model):
    name = models.CharField(max_length=25)
    channel = models.CharField(max_length=15)
    genre = models.CharField(max_length=15)

    def __str__(self):
        return self.name + " - " + self.channel


class Episode(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    episode_name = models.CharField(max_length=25)
    imdb = models.CharField(max_length=5, default='')

    def __str__(self):
        return (self.episode_name + " - (IMDb " + self.imdb + ")")
