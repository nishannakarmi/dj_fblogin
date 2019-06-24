from django.urls import path, include

from login_app.views import sign_up_in, deauth_fb_account

urlpatterns = [
    path('', sign_up_in, name='home'),
    path('accounts/deauth/', deauth_fb_account),
    path('accounts/', include('allauth.urls')),
]
