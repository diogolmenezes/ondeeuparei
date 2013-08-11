from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Reminder(models.Model):
    title = models.CharField(_('title'), max_length=50, null=False)
    place = models.CharField(_('place'), max_length=15, null=False)
    user  = models.ForeignKey(User)