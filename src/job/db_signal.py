from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import WorkInfo,CompanyInfo

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created :
        if not getattr(instance,'workinfo',None):
            WorkInfo.objects.get_or_create(user = instance)
        if not getattr(instance,'companyinfo',None):
            CompanyInfo.objects.get_or_create(user = instance)