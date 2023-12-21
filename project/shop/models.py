from datetime import datetime
from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=64,unique=True)
    category=models.ForeignKey(to='Category',on_delete=models.CASCADE)
    img=models.ImageField(blank=True,upload_to='images')
    type = models.ForeignKey(to='TypeCategory', on_delete=models.CASCADE,blank=True,null=True)
    compound = models.ForeignKey(to='Compound', on_delete=models.CASCADE,blank=True,null=True)

    description = models.TextField()

    length=models.FloatField(default=0)
    width=models.FloatField(default=0)
    price=models.FloatField(default=0.0)
    quantity=models.IntegerField(default=1)
    datetime=models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name=models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.name.title()

class TypeCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()


class Compound(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()

