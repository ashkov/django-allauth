import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import IvranProvider


class IvranAuth2Adapter(OAuth2Adapter):
    provider_id = IvranProvider.id
    access_token_url = "http://localhost:8080/client_credentials.php/access_token"
    authorize_url = "http://localhost:8080/oauth/authorize"
    profile_url = "https://login.ivran.ru/info"

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(
            self.profile_url,
            params={"oauth_token": token.token, "format": "json"},
        )
        resp.raise_for_status()
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(IvranAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(IvranAuth2Adapter)
