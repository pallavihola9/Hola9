import json
from django.conf import UserSettingsHolder
from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Response

from account.models import User

from .models import  adsmangeme, Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# from rest_framework import serializers
# Create your views here.


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
class AdsMessageName(APIView):
  def post(self, request, format=None):
    if not request.data.get("adsid"):
        userid=request.data.get("userid")
        UserIdMail=User.objects.get(pk=userid)
        data=adsmangeme.objects.filter(userid=UserIdMail)
        qs_json = serializers.serialize('json', data)
        for x in data:
          print(x.message)
        print("dataval;uie",data)
        return HttpResponse(qs_json, content_type='application/json')
        return HttpResponse("get request", content_type='application/json')
    userid=request.data.get("userid")
    UserIdMail=User.objects.get(pk=userid)
    adsid=request.data.get("adsid")
    print("!!!user",UserIdMail.email)
    message=request.data.get("message")
    datetime=request.data.get("datetime")
    adsuserid=Product.objects.get(pk=adsid)
    print("@@@userid",adsuserid.user.id)
    print(request.data.get)
    if adsmangeme.objects.filter(userid=userid).filter(adsUserId=adsuserid.user.id):
        # updatemessage=adsmangeme.objects.get(userid=userid).get(adsUserId=adsuserid.user.id)
        # updatemessage.message[datetime]=message
        # updatemessage.save()
        updatemessage=adsmangeme.objects.filter(userid=userid).filter(adsUserId=adsuserid.user.id)
        for x in updatemessage:
            x.message[datetime]=message
            x.save()
            print("x",x.message["232/23/2/3"])
        print("updatemessage",updatemessage)
        # data=json.loads(updatemessage)
        print(type(updatemessage))
        print("already their ",adsmangeme.objects.filter(userid=userid).get(adsUserId=adsuserid.user.id))
        
    else:
        message={}
        message[datetime]=message
        s=adsmangeme.objects.create(userid=UserIdMail,adsUserId=adsuserid.user,message=message)
        print(s.message)
        s.save()
        return HttpResponse("stored in database", content_type='application/json')
        print("not their ")
    return HttpResponse("qs_json", content_type='application/json')
  def get(self,request):
    userid=request.data.get("userid")
    UserIdMail=User.objects.get(pk=userid)
    data=adsmangeme.objects.filter(userid=UserIdMail)
    qs_json = serializers.serialize('json', data)
    for x in data:
        print(x.message)
    print("dataval;uie",data)
    return HttpResponse(qs_json, content_type='application/json')

# @api_view(['GET', 'POST'])
# def AdsMessage(request):
#     print("@@fjdiojfdoi")
#     if request.method=="POST":
#         print("callking")
#         return render ("stored")
