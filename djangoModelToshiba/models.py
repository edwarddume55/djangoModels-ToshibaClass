from __future__ import unicode_literals
from django.db import models


class Toshiba(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=10)


class Meta:
    db_table = "students"
