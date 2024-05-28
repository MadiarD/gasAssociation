from django.urls import path
from .views import ForumPageView, MessagePageView, save_lawyer_message,create_message

urlpatterns = [
    path('', ForumPageView.as_view(), name='forum'),
    path('messages/', MessagePageView.as_view(), name='messages'),
    path('save_lawyer_message/', save_lawyer_message, name='save_lawyer_message'),
    path('create_message/', create_message, name='create_message'),
]
