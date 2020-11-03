# forms.py
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Whitelist


class HonorCodeForm (ModelForm):
    class Meta:
        model = Whitelist
        fields = ['honor_agreement']
        labels = {
            'honor_agreement': _ ('I have read, acknowledge, and agree to the above statements'),
        }
