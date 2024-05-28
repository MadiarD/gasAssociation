from django.contrib import admin
from .models import UserProfile, PaymentAccount, Region

admin.site.register(UserProfile)
admin.site.register(PaymentAccount)
admin.site.register(Region)
