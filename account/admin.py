from django.contrib import admin
from .models import User
# Register your models here.
from .models import PhoneOTP
admin.site.register(PhoneOTP)
admin.site.register(User)