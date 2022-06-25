from django.urls import path
from .views import   updateProfile1, userads, wishlist , userblogs,createFeatured,ordersPyament
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView,ordersPyament,verifyEmail
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('adsby/',userads.as_view(),name='adsby'),
    path('wishlist/',wishlist.as_view(),name='wishlist'),
    path('blogsby/',userblogs.as_view(),name='userblogs'),
    path('updateProfile/',updateProfile1.as_view(),name='update-Profile'),
    path('createFeatured/',createFeatured.as_view(),name='update-createFeatured'),
    path('ordersPyament/',ordersPyament.as_view(),name='update-ordersPyament'),
    path('verifyEmail/',verifyEmail.as_view(),name='update-verifyEmail'),

]