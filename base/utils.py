from django.db import models
from django.contrib.auth.models import  AbstractUser


class Product(models.Model):
    name = models.Charfield(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    postered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    #  properties related to the Vehicle
    make = models.CharField(max_length=500, null=True, blank=True)  # extra for phones,cars etc
    model = models.CharField(max_length=500, null=True, blank=True)  # extra for phones,cars etc
    fuel_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    body_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    transmission = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    mileage = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    conditions = mileage = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    number_of_ownners = mileage = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    colour = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    property_type = models.CharField(max_length=500, null=True, blank=True) 
    #  properties related to property
    seller_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    colour = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    broker_fee = models.BooleanField(default=False)  # extra for vehicles
    plot_size = models.DecimalField(null=True, blank=True)  # extra for vehicles
    erf_size = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    furnishing = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    fenced = models.BooleanField(default=False)  # extra for vehicles
    property_address = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    parking_space = models.BooleanField(default=False)
    security_available = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    bedroom = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    bathroom = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    kitchen = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    lounge = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    dining_room =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    #  properties related to electronics
    brand =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    electronic_model =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    condition =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    #  properties for job
    contact_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    working_hours = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    expiry_date = models.DateTimeField(auto_now=True)
    company_profile = models.TextField(max_length=600, null=True, blank=True)
    job_description = models.TextField(max_length=5000, null=True, blank=True)
    #  properties for clothing and breaty
    product_color = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    gender = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    age_group = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    skin_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    shoe_sizes = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    shoe_sizes = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    dress_sizes = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    general_sizes = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    #  properties on Pets
    pet_age= models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    cat_breed = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    dog_breed = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles