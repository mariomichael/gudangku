# import datetime
# from django.utils import timezone
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    # date_added = models.DateField(default=timezone.now)
    # price = models.IntegerField()
    # description = models.TextField()Z