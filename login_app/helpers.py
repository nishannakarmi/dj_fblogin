def serialize_social_user(user):
    if not user.is_authenticated:
        return {'is_authenticated': False}

    try:
        is_active, profile_picture = user.socialaccount_set.select_related(
            'profile').values_list(
            'profile__is_active', 'profile__profile_picture').first()
        return {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'profile_picture': profile_picture,
            'is_authenticated': True,
            'is_active': is_active,
        }
    except AttributeError:
        return {'is_authenticated': False}
