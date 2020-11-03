# utils.py
from django.conf import settings

from social.exceptions import SocialAuthBaseException, AuthException, AuthForbidden

from .models import Whitelist


def nflrc_load_whitelist(backend, details, response, *args, **kwargs):
	# This method is designed to be called before 'social.pipeline.social_auth.auth_allowed' in the social_auth pipeline. 
	# The method is referenced from the settings. It populates the whitelist from a db query rather that in the clear in the settings file.
	# See: http://python-social-auth.readthedocs.org/en/latest/pipeline.html?highlight=pipelines for more information about this.
    
    settings.SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS = [i.email_addr for i in Whitelist.objects.all()]


class NFLRCAuthForbidden(SocialAuthBaseException):
    """Auth process exception."""
    def __init__(self, backend, response, gaccount, *args, **kwargs):
        self.backend = backend
        self.gaccount = gaccount
        self.response = response
        super(NFLRCAuthForbidden, self).__init__(*args, **kwargs)

    def __str__(self):
        m = self.gaccount
        return m


# def auth_allowed(response, details, *args, **kwargs):
#     """
#     Return the nflrc pbll user object if authenticated email matches a user email in whitelist.
#     whitelist email must match the gmail account (email) used to authenticate.
#     """
#     try:
#     	pbll_user = Whitelist.objects.get(email_addr=details.get('email'))
#         return pbll_user
#     except:
#         return None


def nflrc_auth_allowed(backend, details, response, *args, **kwargs):
    if not backend.auth_allowed(response, details):
        raise NFLRCAuthForbidden(backend, response, details['email'])






