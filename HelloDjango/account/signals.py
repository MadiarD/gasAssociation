from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, PaymentAccount
from members.models import Members
import uuid

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Создание профиля пользователя и платёжного аккаунта при создании нового пользователя
    if created:
        UserProfile.objects.create(user=instance)
        PaymentAccount.objects.get_or_create(user=instance, defaults={'number': uuid.uuid4().int})
    else:
        try:
            instance.profile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
        
        try:
            instance.payment_account.save()
        except PaymentAccount.DoesNotExist:
            PaymentAccount.objects.create(user=instance, number=uuid.uuid4().int)

@receiver(post_save, sender=UserProfile)
def create_or_update_payment_account(sender, instance, created, **kwargs):
    # Создание платёжного аккаунта при создании профиля пользователя
    if created:
        PaymentAccount.objects.get_or_create(user=instance.user, defaults={'number': uuid.uuid4().int})
    else:
        try:
            payment_account = instance.user.payment_account
            payment_account.provider = Members.objects.get(detail__region=instance.region)
            payment_account.save()
        except Members.DoesNotExist:
            print("Provider not found for region:", instance.region)
        except PaymentAccount.DoesNotExist:
            PaymentAccount.objects.create(user=instance.user, number=uuid.uuid4().int)
        except Exception as e:
            print("An error occurred while updating the payment account:", str(e))
