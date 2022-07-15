from contextlib import nullcontext
import json
from site import addsitedir
from tkinter import EW
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
from paymentapi.models import TransationIdone


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

class createFeatured(APIView):
  def post(self, request, format=None):
    image=request.data.get("image")
    user=request.data.get("user")
    title=request.data.get("title")
    price=request.data.get("price")
    tags=request.data.get("tags")
    description=request.data.get("description")
    category=request.data.get("category")
    brand=request.data.get("brand")
    condition=request.data.get("condition")
    state=request.data.get("state")
    city=request.data.get("city")
    locality=request.data.get("locality")
    zip_code=request.data.get("zip_code")
    # date_created=request.data.get("date_created")
    # video=request.data.get("video")
    is_featured=True
    is_active=False
    token=request.data.get("token")
    print(token)
    # print("success value",self.request.session["success"])
    s1=TransationIdone.objects.filter(id1=token)
    print("9999999999999999999999999999999999999999",s1)
    if s1:
      if("succ" in token):
        print("success")
        s=Product.objects.create(image=image,user_id=user,title=title,tags=tags,price=price,description=description,category=category,brand=brand,condition=condition,state=state,city=city,locality=locality,zip_code=zip_code,is_featured=is_featured,is_active=is_active)
        s.save()
        s1=TransationIdone.objects.get(id1=token)
        print(s.pk)
        print("fsedjklfjoisdpljufkl;dsfjkldsfjkl;esdjflksddfjdskl")
        s1.adsid_id=s.pk
        s1.userid_id=user
        s1.save()
      else:
        print("fail path")
        return HttpResponse("fail", content_type='application/json')
    else:
      return HttpResponse("fail", content_type='application/json')
    
    return HttpResponse("success", content_type='application/json')


class ordersPyament(APIView):
  def post(self,request,format=None):
    user=request.data.get("user")
    order=request.data.get("order")
    payment=request.data.get("payment")
    print(order)
    
    s1=Product.objects.filter(user_id=user)
    s=TransationIdone.objects.filter(userid_id=user)
    data = serializers.serialize('json', s1)
    print(data)
    # return HttpResponse(data,content_type='application/json')
    
      
    
    s=TransationIdone.objects.filter(userid_id=user)
    
    # return HttpResponse("unable to fetch",)
    for x in s:
      s1=Product.objects.filter(id=x.adsid_id)
      if s1:
        x.ProductData=serializers.serialize('json', s1)
      data = serializers.serialize('json', s)
      return HttpResponse(data,content_type='application/json')



class verifyEmail(APIView):
    def post(self,request,format=None):
      email=request.data.get("email")
      s=User.objects.filter(email=email)
      if s:
        return HttpResponse("already exist",content_type='application/json')
      else:
        return HttpResponse("not exist",content_type='application/json')



class verifyPhone(APIView):
    def post(self,request,format=None):
      phoneNumber=request.data.get("phoneNumber")
      print(phoneNumber)
      # s1=User.objects.filter(email=email)
      # s=User.objects.filter(phoneNumber=phoneNumber)
      try:
        user = User.objects.get(phoneNumber=phoneNumber)
      except:
        user=None
      if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
      else:
        return Response({'errors':{'non_field_errors':['phone Number not exist']}}, status=status.HTTP_404_NOT_FOUND)
class verifyEmail(APIView):
    def post(self,request,format=None):
      email=request.data.get("email")
      print(email)
      # s1=User.objects.filter(email=email)
      # s=User.objects.filter(phoneNumber=phoneNumber)
      try:
        user = User.objects.get(email=email)
      except:
        user=None
      if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
      else:
        return Response({'errors':{'non_field_errors':['Email not exist']}}, status=status.HTTP_404_NOT_FOUND)
class viewsupdate(APIView):
    def post(self, request, format=None):
        adsID= request.data.get("adsID")
        s = Product.objects.get(pk=adsID)
        s.viewsproduct = s.viewsproduct+1
        s.save()
        return HttpResponse("success", content_type='application/json')          

class updateProfileApi(APIView):
    def post(self, request, format=None):
        user = request.data.get("user")
        print(user)
        if user is None:
          print('address')
          idvalues=request.data.get("idvalues")
          try:
            s=Profile.objects.filter(user_id=idvalues)
            data = serializers.serialize('json', s)
            return HttpResponse(data, content_type='application/json') 
          except:
            s=None
            return HttpResponse("Not exist", content_type='application/json') 
        else:
              image = request.data.get("image")
              user = request.data.get("user")
              name = request.data.get("name")
              email = request.data.get("email")
              PhoneNumber = request.data.get("PhoneNumber")
              print(PhoneNumber)
              address = request.data.get("address")
              state = request.data.get("state")
              city =request.data.get("city")
              zipcode = request.data.get("zipcode")
              print(Profile.objects.filter(user_id=user))
              if Profile.objects.filter(user_id=user) :
                s=Profile.objects.get(user_id=user)
                s.image=image
                s.name=name
                s.email=email
                s.PhoneNumber=PhoneNumber
                s.address=address
                s.state=state
                s.zipcode=zipcode
                s.save()
              else:
                userID = User.objects.get(pk=user)
                s=Profile.objects.create(image=image,user=userID,city=city,name=name,email=email,PhoneNumber=PhoneNumber,address=address,state=state,zipcode=zipcode,)
                s.save()
              return HttpResponse("success", content_type='application/json') 




      

      


