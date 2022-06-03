from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.template.defaultfilters import slugify


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=500, null=True)
    slug = models.SlugField(max_length=600, unique=True, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super(SubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    postered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=2)
    location = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Vehicle(Product):
    #  properties related to the Vehicle
    make = models.CharField(max_length=500, null=True, blank=True)  # extra for phones,cars etc
    model = models.CharField(max_length=500, null=True, blank=True)  # extra for phones,cars etc
    fuel_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    body_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    transmission = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    mileage = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    conditions = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    number_of_ownners = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    colour = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    property_type = models.CharField(max_length=500, null=True, blank=True) 


class Property(models.Model):
     #  properties related to property
    seller_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    colour = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    broker_fee = models.BooleanField(default=False)  # extra for vehicles
    plot_size = models.CharField(max_length=200, null=True, blank=True)  # extra for vehicles
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


class Electronic(models.Model):
    brand =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    electronic_model =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    condition =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles


class Job(models.Model):
    #  properties for job
    contact_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    working_hours = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    expiry_date = models.DateTimeField(auto_now=True)
    company_profile = models.TextField(max_length=600, null=True, blank=True)
    job_description = models.TextField(max_length=5000, null=True, blank=True)
    #  properties for clothing and breaty


class ClothingAndBeauty(models.Model):
    #  properties for clothing and breaty
    product_color = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    gender = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    age_group = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    skin_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    shoe_sizes = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    shoe_sizes = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    dress_sizes = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    general_sizes = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    

class Pet(models.Model):
    #  properties on Pets
    pet_age= models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    cat_breed = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    dog_breed = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles 


class Region(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)


class SubRegion(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)










    
    



