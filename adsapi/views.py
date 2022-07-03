import json
from django.conf import UserSettingsHolder
from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Response
import requests
from account.models import User
import datetime
from .models import  adsmangeme, Product,AdsAdressLatLon,RealEstateEnquery,ReportAds
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# from rest_framework import serializers
# Create your views here.
import ast

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#WishList Views
from .models import WishListItems
from rest_framework.generics import CreateAPIView,DestroyAPIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .serializers import WishListItemsTestSerializer
from django.shortcuts import get_object_or_404
class AddtoWishListItemsView(CreateAPIView,DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishListItems.objects.all()
    serializer_class = WishListItemsTestSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_seller:
            item = get_object_or_404(Product, pk=self.kwargs['pk'])
            serializer.save(owner=user, item=item)
        else:                
            raise serializers.ValidationError("This is not a customer account.Please login as customer.")


    def perform_destroy(self, instance):
        instance.delete()
from django.core import serializers
import ast
class AdsMessageName(APIView):
  def post(self, request, format=None):
    if not request.data.get("adsid"):
        userid=request.data.get("userid")
        UserIdMail=User.objects.get(pk=userid)
        data=adsmangeme.objects.filter(userid=UserIdMail)
        for x in data:
            x.connectMember=x.adsUserId.email
            print("xxxxxxx",x.adsUserId.email)
        qs_json = serializers.serialize('json', data)
        for x in data:
            print(x.message)
            print("dataval;uie",data)
            return HttpResponse(qs_json, content_type='application/json')
    userid=request.data.get("userid")
    UserIdMail=User.objects.get(pk=userid)
    adsid=request.data.get("adsid")
    print("!!!user",UserIdMail.email)
    message=request.data.get("message")
    datetime=request.data.get("datetime")
    adsuserid=Product.objects.get(pk=adsid)
    print("@@@userid",adsuserid.user.id)
    print(request.data.get)
    s=adsmangeme.objects.create(userid=UserIdMail,adsUserId=adsuserid.user,message=message)
    print(s.message)
    s.save()
    # if adsmangeme.objects.filter(userid=userid).filter(adsUserId=adsuserid.user.id):
    #     # updatemessage=adsmangeme.objects.get(userid=userid).get(adsUserId=adsuserid.user.id)
    #     # updatemessage.message[datetime]=message
    #     # updatemessage.save()
    #     updatemessage=adsmangeme.objects.filter(userid=userid).filter(adsUserId=adsuserid.user.id)
    #     for x in updatemessage:
    #         # message={}
    #         # s[datetime]=message
    #         print(x.message)
    #         print(type(x.message))
    #         s=ast.literal_eval(x.message)
    #         print(s)
    #         print(message)
    #         s[datetime]=message
    #         print(s)
    #         x.message=s
    #         x.save()
    #         # print("x",x.message["232/23/2/3"])
    #     print("updatemessage",updatemessage)
    #     # data=json.loads(updatemessage)
    #     print(type(updatemessage))
    #     print("already their ",adsmangeme.objects.filter(userid=userid).get(adsUserId=adsuserid.user.id))
        
    # else:
    #     message={}
    #     message[datetime]=message
    #     s=adsmangeme.objects.create(userid=UserIdMail,adsUserId=adsuserid.user,message=message)
    #     print(s.message)
    #     s.save()
    #     return HttpResponse("stored in database", content_type='application/json')
    #     print("not their ")
    return HttpResponse("qs_json", content_type='application/json')
  def get(self,request):
    userid=request.data.get("userid")
    UserIdMail=User.objects.get(pk=userid)
    
    data=adsmangeme.objects.filter(userid=UserIdMail)
    for x in data:
        x.connectMember=x.adsUserId.email
        print("xxxxxxx",x.adsUserId.email)
    qs_json = serializers.serialize('json', data)
    for x in data:
        print(x.message)
    print("dataval;uie",data)
    return HttpResponse(qs_json, content_type='application/json')


class AdsAdressLatLonView(APIView):
  def get(self, request):
    allads=Product.objects.all()
    for x in allads:
        print("not their ",x.id)
        lat=12.12222
        lon=77.2322
        if(not AdsAdressLatLon.objects.filter(ads=x.id)):
            print("not their ",x.id)
            address=x.locality+x.city+x.state+","+x.zip_code
            print("address value",address)
            # url = "https://address-from-to-latitude-longitude.p.rapidapi.com/geolocationapi"
            # querystring = {"address":address}
            # headers = {
	        #     "X-RapidAPI-Key": "331734c762msh87686d3f66d810fp1c85ebjsn31d2ac2b6d68",
	        #     "X-RapidAPI-Host": "address-from-to-latitude-longitude.p.rapidapi.com"
            # }
            # response = requests.request("GET", url, headers=headers, params=querystring)
            # print("ads latitude longtitude",response.text)
            # print(response.text)
            s=AdsAdressLatLon.objects.create(ads_id=x.id,lat=lat+2,lon=lon+2)
            s.save()
        else:
            print("else block ")
    jsonLatLonData=AdsAdressLatLon.objects.all()
    qs_json = serializers.serialize('json', jsonLatLonData)
    return HttpResponse(qs_json, content_type='application/json')


class chatMessages(APIView):
  def post(self, request, format=None):
    # s=adsmangeme.objects.all().delete()
    userid=request.data.get("userid")
    adsUserEmail=request.data.get("adsUserEmail")
    print("values printing userid adsuseremail",userid,adsUserEmail)
    s=User.objects.get(email=adsUserEmail)
    print("user id ads ",s.pk)
    messageData=adsmangeme.objects.filter(userid=userid,adsUserId=s.pk)
    # for x in messageData:
    #     print(x.message)
    #     print(type(x.message))
        # print( ast.literal_eval(x.message))
        # print(type( ast.literal_eval(x.message)))
        # print(json.dumps(ast.literal_eval(x.message)))
        # data=json.dumps(ast.literal_eval(x.message))
    qs_json = serializers.serialize('json', messageData)
    return HttpResponse(qs_json, content_type='application/json')
# @api_view(['GET', 'POST'])
# def AdsMessage(request):
#     print("@@fjdiojfdoi")
#     if request.method=="POST":
#         print("callking")
#         return render ("stored")

class chatting(APIView):
  def post(self, request, format=None):
    sender=request.data.get("sender")
    reciever=request.data.get("reciever")
    # senderEmailId=User.objects.get(pk=sender)
    # print("senderEmailid",senderEmailId)
    message=request.data.get("message")
    print("fdfjdsl")
    # datetime=str(datetime.datetime.now())
    s=adsmangeme.objects.create(userid=User.objects.get(email=sender),adsUserId=User.objects.get(email=reciever),message=message,connectMember=sender)
    s.save()
    # qs_json = serializers.serialize('json', messageData)
    return HttpResponse("qs_json", content_type='application/json')


class uploadImages(APIView):
    def post(self, request, format=None):
        imagelist=request.data.get("imageList")
        adsid=request.data.get("adsid")
        s=Product.objects.get(pk=adsid)
        print(imagelist)
        # for x in imagelist:
        return HttpResponse("qs_json", content_type='application/json')

class RealEstateEnquery1(APIView):
    def post(self, request, format=None):
        firstName=request.data.get("firstName")
        lastName=request.data.get("lastName")
        email=request.data.get("email")
        zip_code=request.data.get("zip_code")
        s=RealEstateEnquery.objects.create(firstName=firstName,lastName=lastName,email=email,zip_code=zip_code)
        s.save()
        return HttpResponse("sucess", content_type='application/json')


class ReportAds1(APIView):
    def post(self, request, format=None):
        ads=request.data.get("ads")
        adsModel=Product.objects.get(pk=ads)
        reportMessage=request.data.get("report")
        s=ReportAds.objects.create(ads=adsModel,report=reportMessage)
        s.save()
        return HttpResponse("sucess", content_type='application/json')


class AdsUpload(APIView):
    def post(self, request, format=None):
        imageList=request.data.file("imageList")
        adsiD= request.data.get("adsId")
        # imageList1=request.data.get("imageList1")
        print("@@@@imagelist data ,ads id",imageList,adsiD)
        print("image view",list(imageList))
        return HttpResponse("sucess", content_type='application/json')