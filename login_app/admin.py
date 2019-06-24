from django.contrib import admin

from login_app.models import SocialUserProfile


class SocialUserProfileAdmin(admin.ModelAdmin):
    list_display = ('social_account', 'profile_picture', 'is_active')


admin.site.register(SocialUserProfile, SocialUserProfileAdmin)
