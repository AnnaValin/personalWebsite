# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#mysite_contact
class Contact(models.Model):
	name = models.CharField(max_length=50, null=True)
	lastName = models.CharField(max_length=50, null=True)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()

	def __str__(self):
		return self.email