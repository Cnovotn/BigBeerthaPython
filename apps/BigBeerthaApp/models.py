# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt

class User(models.Model):
    media_type = models.CharField(max_length=10)# either image, or video
    link = models.CharField(max_length=245)
