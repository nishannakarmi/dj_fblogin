from django.test import TestCase

from login_app.utils import decode_signed_request


class UtilTest(TestCase):
    def setUp(self):
        self.secret = '897z956a2z7zzzzz5783z458zz3z7556'
        self.signed_request = 'gI7hojzSUZyrEP6/kh7TRCI6PZ6VucX0bvbcKxj10HY.'\
                              'eyJ1c2VyX2lkIjoiMTExMTExMSJ9'
        self.test_user_id = '111111'

    def test_decode_successfully(self):
        data = decode_signed_request(self.signed_request, self.secret)
        self.assertEqual(self.test_user_id, data['user_id'])
