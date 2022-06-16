from django.urls import path
from .views import checkOTP , otpGeneration 


urlpatterns = [
    path('checkOTP/', checkOTP ),
    path('sendOTP/',otpGeneration),
]