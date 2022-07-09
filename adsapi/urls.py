from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import  AdsMessageName,blogCommentBoxView, AdsUpload,ProductView ,ReportAds1, AddtoWishListItemsView,AdsAdressLatLonView,chatMessages,chatting,uploadImages,RealEstateEnquery1,adsCommentBoxView

route = routers.DefaultRouter()
route.register("",ProductView,basename='productview')

urlpatterns = [
    path('',include(route.urls)),
    #WishList URLS
    path('api/addwishlistitems/<int:pk>', AddtoWishListItemsView.as_view(),name='add-to-wishlist'),
    path('AdsMessage', AdsMessageName.as_view(),name='add-to-message'),
    path('AdsAdressLatLon', AdsAdressLatLonView.as_view(),name='add-to-address'),
    path('chatMessages', chatMessages.as_view(),name='add-to-ChatMessage'),
    path('chatting', chatting.as_view(),name='add-to-chatting'),
    path('uploadImages', uploadImages.as_view(),name='add-to-uploadImages'),
    path('RealEstateEnquery', RealEstateEnquery1.as_view(),name='add-to-RealEstateEnquery'),
    path('ReportAds', ReportAds1.as_view(),name='add-to-ReportAds'),
    path('adsUpload', AdsUpload.as_view(),name='add-to-adsUpload'),
    path('adsCommentBox', adsCommentBoxView.as_view(),name='add-to-adsCommentBox'),
    path('blogCommentBox', blogCommentBoxView.as_view(),name='add-to-blogCommentBox')
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

