from django.db import models

# Create your models here.


class Product(models.Model):
    # id = models.autoField()
    title = models.CharField(max_length=220)
    content = models.CharField(null=True, blank=True, max_length=220)
    price = models.IntegerField(default=0)
