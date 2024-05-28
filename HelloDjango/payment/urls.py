from django.urls import path
from .views import CalculationPageView, yookassa_notification
urlpatterns = [
        path('calculation',CalculationPageView.as_view(),name = 'calculation'),
        path('yookassa/', yookassa_notification, name='yookassa_notification'),
]