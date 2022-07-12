from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.template.defaultfilters import slugify
from  .options_classes.options_list.vechicle_option_lists import  * 
from .options_classes.options_list.property_option_lists import *
from .options_classes.options_list.electronic_option_lists import *
from .options_classes.options_list.beauty_options_lists import *
from .options_classes.options_list.job_option_lists import *
from .options_classes.options_list.pet_options_list import *




# class VehicleModel:
#     def __init__(self,model, fuel_type):
#         self.model = model
#         self.fuel_type
    

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
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    # the category1 will be used for our serializers 
    # category1 = models.ForeignKey(Category, related_name='subcategory1', on_delete=models.SET_NULL,
    #  null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)


#  Refers to properties to search for brands, make, vehicles
class Type(models.Model):
    type_name = models.CharField(max_length=200, null=True, blank=True)
    # image = models.ImageField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.type_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.type_name)
        super(Type, self).save(*args, **kwargs)


class Region(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.name)
       super(Region, self).save(*args, **kwargs)
        

class SubRegion(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=300, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubRegion, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    postered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    #  type represent brand, make, property type, etc
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=2)
    #  location = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    subregion = models.ForeignKey(SubRegion, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
            


class Vehicle(Product):
    #  properties related to the Vehicle
    #  make = models.CharField(max_length=500, null=True, blank=True)  # extra for phones,cars etc
    model = models.CharField(max_length=500, null=True, blank=True)  # extra for phones,cars etc
    fuel_type = models.CharField(max_length=500, choices=fuel_type_dropdown, null=True, blank=True)  # extra for vehicles
    body_type = models.CharField(max_length=500, choices=body_type_dropdown, null=True, blank=True)  # extra for vehicles
    transmission = models.CharField(max_length=500, choices=transmission_dropdown, null=True, blank=True)  # extra for vehicles
    mileage = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    conditions = models.CharField(max_length=500, choices=condition_dropdown, null=True, blank=True)  # extra for vehicles
    number_of_ownners = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    colour = models.CharField(max_length=500, choices=vehicle_colour_dropdown, null=True, blank=True)  # extra for vehicles
    #  property_type = models.CharField(max_length=500, null=True, blank=True) 


class Property(Product):
     #  properties related to property
    #  property_type = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    #  colour = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    seller_type = models.CharField(max_length=200, choices=seller_type_dropdown, null=True, blank=True)
    broker_fee = models.BooleanField(default=False)  # extra for vehicles
    #  broker_fee = models.CharField(max_length=200, choices=broker_fee_dropdown, null=True, blank=True)  # extra for vehicles
    plot_size = models.CharField(max_length=200, null=True, blank=True)  # extra for vehicles
    erf_size = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    furnishing = models.CharField(max_length=500, choices=furnishing_dropdown, null=True, blank=True)  # extra for vehicles
    fenced = models.BooleanField(default=False)  # extra for vehicles
    property_address = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    parking_space = models.BooleanField(default=False)
    security_available = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    bedroom = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    bathroom = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    kitchen = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    lounge = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    dining_room =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles


class Electronic(Product):
    #  brand will be represented by type whicjh is in the Product class
    #  brand =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    electronic_model =  models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    condition =  models.CharField(max_length=500, choices=condition_dropdown, null=True, blank=True)  # extra for vehicles


class Job(Product):
    #  properties for job
    contact_type = models.CharField(max_length=500, choices=contract_type_dropdown, null=True, blank=True)  
    working_hours = models.CharField(max_length=500, choices=working_hours_dropdown, null=True, blank=True)
    #  working_hours will be used to display products on top 
    #  working_hours = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)
    expiry_date = models.DateTimeField(auto_now=True)
    company_profile = models.TextField(max_length=600, null=True, blank=True)
    job_description = models.TextField(max_length=5000, null=True, blank=True)


class ClothingAndBeauty(Product):
    #  properties for clothing and breaty
    product_color = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    gender = models.CharField(max_length=500, choices=gender_dropdown, null=True, blank=True)  # extra for vehicles
    age_group = models.CharField(max_length=500, choices=age_group_dropdown, null=True, blank=True)  # extra for vehicles
    skin_type = models.CharField(max_length=500, choices=skin_type_dropdown, null=True, blank=True)  # extra for vehicles
    shoe_sizes = models.CharField(max_length=500, choices=shoe_sizes_dropdown,null=True, blank=True)  # extra for vehicles
    dress_sizes = models.CharField(max_length=500, choices=dress_sizes_dropdown, null=True, blank=True)  # extra for vehicles
    general_sizes = models.CharField(max_length=500, choices=general_dropdown, null=True, blank=True)  # extra for vehicles
    #  size = models.CharField(max_length=500, null=True, blank=True)  # extra for vehicles
    

class Pet(Product):
    #  properties on Pets
    #  its type will represent a breed eg dog will have bulldog as breed
    pet_age= models.CharField(max_length=500, choices=age_dropdown, null=True, blank=True)  # extra for vehicles
    cat_breed = models.CharField(max_length=500, choices=cat_breed_dropdown, null=True, blank=True)  # extra for vehicles
    dog_breed = models.CharField(max_length=500, choices=dog_breed_dropdown, null=True, blank=True)  # extra for vehicles 


#class 
