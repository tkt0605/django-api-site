from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Account, CustomUser
from rest_framework.authtoken.models import Token
User =  get_user_model()
@receiver(post_save, sender=get_user_model())
def create_user_account(instance, created, **kwargs):
    if created:
        return Account.objects.create(email=instance, name=instance.username)

# @receiver(post_save, sender=get_user_model())
# def create_token(instance, created, **kwargs):
#     if created:
#         return Token.objects.create(user=instance)
@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created and instance is not None:
        Token.objects.create(user=instance)