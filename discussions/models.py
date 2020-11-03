from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

from model_utils.models import TimeStampedModel



class Post(TimeStampedModel):
    text = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=512)
    parent_post = models.ForeignKey('self', blank=True, null=True, related_name='replies', on_delete=models.CASCADE )
    deleted = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def get_reply_form(self, creator_init=None):
        from .forms import PostSubthreadReplyForm
        initial_post_reply_data = {}
    
        initial_post_reply_data['creator'] = creator_init
        initial_post_reply_data['subject'] = 'Re: %s'% self.subject
        initial_post_reply_data['parent_post'] = self.id  
        return PostSubthreadReplyForm(initial=initial_post_reply_data)

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self.subject))
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.subject


class DiscussionLog(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.modified)

