from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager
from datetime import datetime

from django.core.files.storage import FileSystemStorage
import os
from sys import platform
import uuid


def upload_location(instance, filename):
    filebase, extension = filename.split(".")[-1]
    randname=uuid.uuid4().hex
    print extension
    return "%s.%s" %(randname, extension)

class CustomerModel(models.Model):
    STATUS_CHOICES = (
        (1,'Active'),
        (0,'Inactive')
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_location,null=True,blank=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)
