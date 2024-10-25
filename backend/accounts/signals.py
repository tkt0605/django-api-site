from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Account, CustomUser
User =  get_user_model()
@receiver(post_save(sender=User))
def create_user_account(self, instance, created, **kwargs):
    if created:
        return Account.objects.create(email=instance, name=instance.username)
