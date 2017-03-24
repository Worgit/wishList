from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserManager(models.Manager):
	def validation(self,name, username, password, confirm):
		retlist = []
		##print "*"*80
		if len(name) < 3:
			##print "*"*40
			retlist.append("First Name Too Short.")
		if len(username) < 3:
			##print "*"*35
			retlist.append("Last Name Too Short.")
		if len(password) < 8:
			##print "*"*20
			retlist.append("Password Too Short.")
		if password != confirm:
			##print "*"*15
			retlist.append("Password does not match confirmation.")
		if len(retlist) == 0:
			return "Success"
		return retlist

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	date = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
