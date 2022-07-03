from django.urls import path
from .views import checkOTP , otpGeneration ,verifyUserPhone


urlpatterns = [
    path('checkOTP/', checkOTP ),
    path('sendOTP/',otpGeneration),
    path('verifyUserPhone',verifyUserPhone)
]