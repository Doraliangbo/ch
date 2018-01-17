from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class City(models.Model):

class StateOrProvince()models.Model):


class Resturant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    rate = models.PositiveSmallIntegerField()
    website = models.URLField(max_length=100)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.ForeignKeyField(City, on_delete=models.CASCADE)
    stateorprovince = models.ForeignKeyField(StateorProvince, on_delete=models.CASCADE)
    

class Menu(models.Model):
    type = models.CharField(max_length=100)
    resturant = models.ForeignKeyField(Resturant, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)

class MenuSection(models.Model):
    section_name = models.CharField(max_length=100)
    menu = models.ForeignKeyField(Menu, on_delete=models.CASCADE)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKeyField(MenuSection, on_delete=models.CASCADE))
    rate = models.PositiveSmallIntegerField()
    


