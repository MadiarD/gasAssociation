from django.db import models
from django.contrib.auth.models import User
from members.models import Members
import uuid 
class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class PaymentAccount(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number = models.CharField(max_length=20, unique=True,null=True,default=uuid.uuid4().int)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='payment_account')
    provider = models.ForeignKey(Members, on_delete=models.CASCADE, null=True, blank=True)
    last_meter_indicator = models.DecimalField(max_digits=8, decimal_places=3, default=0) 
    meter_indicator = models.DecimalField(max_digits=8, decimal_places=3, default=0)

    def __str__(self):
        return f"{self.user} {self.number}"

class UserProfile(models.Model):
    USER_ROLE_CHOICES = [
        ('user', 'Обычный пользователь'),
        ('lawyer', 'Юрист'),
        ('admin', 'Админ'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=20, blank=True, null=True)
    apartment = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='user')
    

    def __str__(self):
        return self.user.username



