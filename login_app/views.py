# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse
from django.http import JsonResponse

from allauth.socialaccount.models import SocialAccount

from login_app.exceptions import BadSignatureException
from login_app.helpers import serialize_social_user
from login_app.utils import decode_signed_request


def sign_up_in(request):
    """
    it will be rendered the same html content but some conditions exist in html
    whether user is authenticated or not
    """
    user = request.user
    context = serialize_social_user(user)
    return render(request, 'sign_up_in.html', context)


@require_http_methods(['POST'])
def deauth_fb_account(request):
    try:
        data = decode_signed_request(request.POST.get('signed_request'),
                                     settings.SOCIAL_AUTH_FACEBOOK_SECRET)
    except BadSignatureException as e:
        # raise bad request with regarding message
        return HttpResponse(status=400, content=e.message)

    # find socialaccount and social profile accordingly
    # and deactivate user
    user_id = data['user_id']
    profile = SocialAccount.objects.select_related(
        'profile').get(uid=user_id).profile
    profile.deactivate()

    return JsonResponse({'uid': user_id, 'deactivated': True})
