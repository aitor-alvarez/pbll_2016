from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel

PARTICIPANT_TYPES = (
	('opt1', 'Option 1'),
	('opt2', 'Option 2'),
	('staff', 'Staff')
)

class Whitelist(TimeStampedModel):
	email_addr = models.EmailField(max_length=254, unique=True)
	honor_agreement = models.BooleanField(default=False)
	participant_type = models.CharField(max_length=8, choices=PARTICIPANT_TYPES, default='opt2')
	site_account = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.email_addr

class SiteFile(TimeStampedModel):
    fileobj = models.FileField(upload_to='pbll-media')

    def __unicode__(self):
        return self.fileobj
  
