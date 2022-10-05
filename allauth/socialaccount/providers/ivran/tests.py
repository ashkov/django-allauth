from __future__ import absolute_import

from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase

from .provider import IvranProvider


class IvranTests(OAuth2TestsMixin, TestCase):
    provider_id = IvranProvider.id

    ivran_data = """
        {
            "login": "vasya",
                "old_social_login": "uid-mmzxrnry",
                    "default_email": "test@ivran.ru",
                        "id": "1000034426",
                            "client_id": "4760187d81bc4b7799476b42b5103713",
                                "emails": [
                                    "test@ivran.ru",
                                    "other-test@ivran.ru"
                                ],
                                "openid_identities": [
                                    "http://openid.ivran.ru/vasya/",
                                    "http://vasya.ya.ru/"
                                ]
        }"""

    def get_mocked_response(self, data=None):
        if data is None:
            data = self.ivran_data
        return MockedResponse(200, data)

    def get_login_response_json(self, with_refresh_token=True):
        return """
            {
                "access_token":"testac",
                "refresh_token":"1:GN686QVt0mmakDd9:A4pYuW9LGk0_UnlrMIWklk",
                "token_type":"bearer",
                "expires_in":124234123534
            }"""
