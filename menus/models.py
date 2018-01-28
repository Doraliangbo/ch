from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class City(models.Model):
    name = models.CharField("City name",max_length=50) #City name is row name

    def __str__(self):                                 #__str__ give the display name
        return self.name

class StateOrProvince(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class MenuSection(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Resturant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    rate = models.PositiveSmallIntegerField()
    website = models.URLField(max_length=100)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    stateorprovince = models.ForeignKey(StateOrProvince, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20, default="000-000-0000")
    def __str__(self):
        return self.name +" ["+ self.phonenumber + "]"
    

class Menu(models.Model):
    mtype = models.CharField(max_length=100)
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE)


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField()
    menusection = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    


