from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id','title','price','tags','brand','condition','state','date_created')