from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=70)
    Email = models.EmailField(max_length=80)
    PhoneNumber = models.IntegerField()
    Message = models.TextField()
