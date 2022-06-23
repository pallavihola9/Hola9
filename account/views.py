import json
from site import addsitedir
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adsapi.models import Product
from blogsapi.models import Blogs
from adsapi.serializers import ProductSerializer
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
import random
import http.client

from profileapi.models import Profile
from .models import PhoneOTP , User
import ast

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)


from django.core import serializers

class userads(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    print(request.user.id)
    adsData=Product.objects.filter(user =request.user)
    print("adsData",adsData)
    serializer = serializers.serialize('json', adsData)
    print(serializer)
    qs_json = serializers.serialize('json', adsData)
    return HttpResponse(qs_json, content_type='application/json')

class userblogs(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    print(request.user.id)
    blogsData=Blogs.objects.filter(user =request.user)
    print("blogsData",blogsData)
    serializer = serializers.serialize('json', blogsData)
    print(serializer)
    qs_json = serializers.serialize('json', blogsData)
    return HttpResponse(qs_json, content_type='application/json')


class wishlist(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    wishlist=request.data.get('wishlist')
    print(wishlist)
    wishlist=wishlist+","
    newlist=[]
    y=""
    for x in wishlist:
      if x!=",":
        y=y+x
      else:
        newlist.append(int(y))
        print("value",newlist)
        y=""
    print(newlist)
    # print("@@WISHLIST",type(list(wishlist)))
    # wishlist=list(wishlist)
    # print("starting")
    # # wishlist=wishlist.remove(',')
    # print(wishlist)
    # wishlistone=[]
    # for x in wishlist:
    #   if x!=',':
    #     wishlistone.append(int(x))
    # print("current wishlist",wishlistone)
    # res = []
    # for i in wishlistone:
    #   if i not in res:
    #       res.append(i)
    # print("res",res)

    wishlist=Product.objects.filter(pk__in=newlist)
    print("@@findal dat in wishlist ",wishlist)
    wishlist = serializers.serialize('json', wishlist)
    return HttpResponse(wishlist, content_type='application/json')




class updateProfile1(APIView):
  def post(self, request, format=None):
    email=request.data.get("email")
    s=Profile.objects.filter(email=email)
    print(type(s))
    if(s):
      profile = serializers.serialize('json', s)
      return HttpResponse(profile, content_type='application/json')
    return HttpResponse("false", content_type='application/json')


