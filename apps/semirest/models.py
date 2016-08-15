from __future__ import unicode_literals
from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
