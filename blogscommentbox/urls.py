from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import BlogsCommentView

route = routers.DefaultRouter()
route.register("",BlogsCommentView,basename='AdsCommentView')

urlpatterns = [
    path('',include(route.urls)),
]

