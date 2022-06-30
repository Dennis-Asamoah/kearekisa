from django.db import models
from base.models import *


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='vehicle_image',
     on_delete=models.SET_NULL, null=True, blank=True
     )
    image = models.ImageField(upload_to='vehicle/')


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', 
    on_delete=models.SET_NULL, null=True, blank=True
    )
    image = models.ImageField(upload_to='property/')


class ElectronicImage(models.Model):
    Electronic = models.ForeignKey(Electronic, related_name='electronic_image',
     on_delete=models.SET_NULL, null=True, blank=True
     )
    image = models.ImageField(upload_to='electronic/')


class JobImage(models.Model):
    job = models.ForeignKey(Job, related_name='job_image',
     on_delete=models.SET_NULL, null=True, blank=True
     )
    image = models.ImageField(upload_to='job/')


class ClothingAndBeautyImage(models.Model):
    clothingandbeauty = models.ForeignKey(ClothingAndBeauty, related_name='clothingandbeauty_image', 
    on_delete=models.SET_NULL, null=True, blank=True
    )
    image = models.ImageField(upload_to='clothingandbeauty/') 


class PetImage(models.Model):
    pet  = models.ForeignKey(Pet, related_name='pet_image', 
    on_delete=models.SET_NULL, null=True, blank=True
    )
    image = models.ImageField(upload_to='pet/')
