from django.contrib import admin
from .models import  *

@admin.register(Electronic)
class ElectronicAdmin(admin.ModelAdmin):
    #  exclude = ('condition', )  # ','ticket_status','ticket_end ')
    pass


# @admin.register(Vehicle)
# class VehicleAdmin(admin.ModelAdmin):
#     list_display = ()

# Register your models here.
admin.site.register(User)
#admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'date')

admin.site.register(SubCategory)
admin.site.register(Vehicle)
admin.site.register(Property)
#  admin.site.register(Electronic)
admin.site.register(Job)
admin.site.register(Pet)
admin.site.register(Region)
admin.site.register(SubRegion)
admin.site.register(ClothingAndBeauty)
admin.site.register(Type)
