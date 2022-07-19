from django.contrib import admin
from .models import Product,ImageAdsModels
# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id','title','price','tags','brand','condition','state','date_created')
admin.site.register(ImageAdsModels)