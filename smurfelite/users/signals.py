import profile
from venv import create
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile, User



# this signal will create a profile for a new user with name,email,username instance
@receiver(post_save, sender=User)
def create_profile_user(sender, instance, created, *args, **kwargs):
    if created:
        user = instance
        Profile.objects.create(
            user=user,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )


# this signal will update the user's name,email,username, if updated through profile form by user.
@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, *args, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = (profile.first_name,)
        user.last_name = profile.l_name
        user.username = profile.username
        user.email = profile.email
        user.save()
