from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import  AdsMessageName, ProductView , AddtoWishListItemsView

route = routers.DefaultRouter()
route.register("",ProductView,basename='productview')

urlpatterns = [
    path('',include(route.urls)),
    #WishList URLS
    path('api/addwishlistitems/<int:pk>', AddtoWishListItemsView.as_view(),name='add-to-wishlist'),
    path('AdsMessage', AdsMessageName.as_view(),name='add-to-message'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

