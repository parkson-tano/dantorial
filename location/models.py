from django.db import models
# from cities_light.abstract_models import (AbstractCity, AbstractRegion,
    # AbstractCountry, AbstractSubRegion )

# from cities_light.receivers import connect_default_signals
# Create your models here.
# class Country(AbstractCountry):
#     pass
# connect_default_signals(Country) 

#     # def __str__(self):
#     #     return self.name

# class Region(AbstractRegion):
#     pass

# connect_default_signals(Region)

# class City(AbstractCity):
#     pass
# connect_default_signals(City)

# class SubRegion(AbstractSubRegion):
#     pass
# connect_default_signals(SubRegion)

class Country(models.Model):
    name = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Town(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Quater(models.Model):
    # town = models.ForeignKey(Town, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name