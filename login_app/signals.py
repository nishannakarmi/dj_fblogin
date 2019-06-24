from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from login_app.models import SocialUserProfile


@receiver(user_signed_up)
def user_signup_handler(sender, request, user, **kwargs):
    # used limit-offset for faster query
    social_account = user.socialaccount_set.first()
    profile_picture = social_account.extra_data.get(
        'picture', {}).get('data', {}).get('url')
    SocialUserProfile.objects.create(social_account=social_account,
                                     profile_picture=profile_picture)
