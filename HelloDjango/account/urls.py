
from django.urls import path
from django.urls.conf import include
from account.views import RegisterView, save_inf, save_address_inf, ProfilePageView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('form/inf/', save_inf, name='save_inf'),
    path('form/address_inf/', save_address_inf, name='save_address_inf'),
    path('profile',ProfilePageView.as_view(),name = 'profile'),
]
