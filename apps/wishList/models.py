from __future__ import unicode_literals

from django.db import models
from ..loginApp.models import User
# Create your models here.

class ItemManager(models.Manager):
	def validation(self,name):
		retlist = []
		##print "*"*80
		if len(name) < 4:
			##print "*"*40
			retlist.append("Name Too Short.")
		if len(retlist) == 0:
			return "Success"
		return retlist

class Item(models.Model):
	name = models.TextField(max_length=255)
	wishes = models.ManyToManyField(User, related_name = "items")
	creator = models.ForeignKey(User, related_name = "items_created")
	date = models.DateField(auto_now_add = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = ItemManager()