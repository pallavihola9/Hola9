from unicodedata import category
from django.db import models
from embed_video.fields import EmbedVideoField
from account.models import User
from jsonfield import JSONField
from picklefield.fields import PickledObjectField
# Create your models here.
STATE_CHOICES = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh' , 'Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujrat','Gujrat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharastra','Maharastra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telengana','Telengana'),
    ('Tripura','Tripura'),
    ('Uttarkhand','Uttarkhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
)

class Product(models.Model):
    CONDITION = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
    )
    image = models.ImageField(upload_to ='upload/images',null=False,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=150,null=False,blank=False)
    price = models.DecimalField(max_digits=7,decimal_places=2,null=False,blank=False)
    tags = models.CharField(max_length=150,null=False,blank=False)
    description = models.TextField()
    category = models.CharField(max_length=50,null=True,blank=True)
    brand = models.CharField(max_length=200)
    condition = models.CharField(max_length=100, choices=CONDITION)
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    city = models.CharField(max_length=50)
    locality = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=6)
    date_created = models.DateTimeField(auto_now_add=True)
    video = EmbedVideoField(null=True, blank=True) 
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    subCategoryType=models.CharField(default="null",max_length=3232)
    subCategoryValue=models.CharField(default="null",max_length=3232)

#Wishlist Models
class WishListItems(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    #wishlist = models.ForeignKey(WishList,on_delete=models.CASCADE, related_name='wishlistitems')
    item = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)  


# class AdsMessage(models.Model):
#     userid=models.ForeignKey(User,related_name='related_primary_manual_roats', on_delete=models.CASCADE)
#     adsUserId=models.ForeignKey(User, related_name='related_secondary_manual_roats',on_delete=models.CASCADE)
#     message=models.JSONField()
# class AdsMessagename(models.Model):
#     userid=models.ForeignKey(User,related_name='related_primary_manual_roats', on_delete=models.CASCADE)
#     adsUserId=models.ForeignKey(User, related_name='related_secondary_manual_roats',on_delete=models.CASCADE)
#     message=models.TextField()

class adsmangeme(models.Model):
    userid=models.ForeignKey(User,related_name='related_primary_manual_roats', on_delete=models.CASCADE)
    adsUserId=models.ForeignKey(User, related_name='related_secondary_manual_roats',on_delete=models.CASCADE)
    message=models.TextField()
    connectMember=models.CharField(max_length=223232,default="srishtisrija@gmail.com")

class AdsAdressLatLon(models.Model):
    ads=models.ForeignKey(Product, on_delete=models.CASCADE)
    lat=models.IntegerField()
    lon=models.IntegerField()

class ImageAdsModels(models.Model):
    ads= models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True) 
    image=models.ImageField(upload_to ='upload/images',null=False,blank=False) 

class RealEstateEnquery(models.Model):
    firstName=models.CharField(max_length=232)
    lastName=models.CharField(max_length=232)
    email=models.CharField(max_length=343)
    zip_code=models.CharField(max_length=232)

class ReportAds(models.Model):
    ads= models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    report=models.CharField(max_length=23222)




