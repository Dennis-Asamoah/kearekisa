from django.contrib import admin
from .models import  *

@admin.register(Electronic)
class ElectronicAdmin(admin.ModelAdmin):
    exclude = ('condition', )  # ','ticket_status','ticket_end ')

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
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
