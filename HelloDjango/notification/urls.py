
from django.urls import path
from .views import notifications_page, get_notifications

urlpatterns = [
    path('', notifications_page, name='notifications_page'),
    path('get/', get_notifications, name='get_notifications'),
]
