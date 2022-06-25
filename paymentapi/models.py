from django.db import models

from adsapi.models import Product
from account.models import User
# Create your models here.

class Order(models.Model):
    user_email=models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=25)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class TransationIdone(models.Model):
    id1=models.CharField(max_length=2322)
    dateid=models.CharField(max_length=232)
    message=models.CharField(max_length=232)
    adsid=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    userid=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ProductData=models.CharField(max_length=43343333,null=True)

