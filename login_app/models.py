# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allauth.socialaccount.models import SocialAccount
from django.db import models


class SocialUserProfile(models.Model):
    social_account = models.OneToOneField(
        SocialAccount, on_delete=models.CASCADE,
        primary_key=True, related_name='profile')
    is_active = models.BooleanField(default=True)
    profile_picture = models.TextField(null=True, blank=True)

    def deactivate(self):
        # make user de-active
        self.is_active = False
        self.save()
