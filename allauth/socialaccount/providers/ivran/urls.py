from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import IvranProvider


urlpatterns = default_urlpatterns(IvranProvider)
