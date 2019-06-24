import base64
import hashlib
import hmac
import json

from login_app.exceptions import BadSignatureException


def decode_signed_request(signed_request, secret):
    """
    decode signed data from facebook post and find user info
    example signed_request: 2154adsads.dotritirratf755
    """
    if not signed_request:
        raise BadSignatureException('signed_request is missing.')

    try:
        encoded_sig, payload = signed_request.split('.')
    except ValueError:
        raise BadSignatureException('signed_request is malformed.')

    try:
        sig = decode_fb_encoded_str(encoded_sig)
    except TypeError:
        raise BadSignatureException(
            'encoded_sig is malformed, incorrect padding.')

    try:
        data_encoded = decode_fb_encoded_str(payload)
        data = json.loads(data_encoded)
    except (TypeError, ValueError):
        raise BadSignatureException(
            'payload is malformed, incorrect padding or '
            'incorrect json format.')

    expected_sig = hmac.new(
        secret, msg=payload, digestmod=hashlib.sha256).digest()
    if sig != expected_sig:
        raise BadSignatureException('exploit!')

    return data


def decode_fb_encoded_str(encoded):
    """
    fix padding first, then decode url safe replacing url safe chars
    """
    encoded = fix_padding_4_b64(encoded)
    return base64.urlsafe_b64decode(encoded)


def fix_padding_4_b64(encoded):
    """
    add missing `=`
    """
    length = len(encoded)
    modulo = length % 4
    missed_part_count = 4 - modulo if modulo != 0 else 0
    return '{}{}'.format(encoded, '=' * missed_part_count)
