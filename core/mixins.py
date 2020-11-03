# mixins.py
from django.shortcuts import redirect

from .models import Whitelist

class HonorCodeRequired(object):
    def dispatch(self, *args, **kwargs):
    	activated = Whitelist.objects.get(email_addr=self.request.user.email).honor_agreement
    	if not activated:
    		return redirect('honor_agreement')
    	return super(HonorCodeRequired, self).dispatch(*args, **kwargs)