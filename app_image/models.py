from django.db import models
from base.models import *


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='vehicle/')


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='property/')


class ElectronicImage(models.Model):
    Electronic = models.ForeignKey(Electronic, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='electronic')


class JobImage(models.Model):
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='job/')


class ClothingAndBeautyImage(models.Model):
    clothingandbeauty = models.ForeignKey(ClothingAndBeauty, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='clothingandbeauty/') 


class PetImage(models.Model):
    pet  = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='pet/')
