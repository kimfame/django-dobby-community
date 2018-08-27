from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
	title = models.CharField(max_length=200)
	nickname = mdoels.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
	hit = models.PositiveIntegerField(default=0)
	#like_count = models.PositiveIntegerField(default=0)
	#unlike_count = models.PositiveIntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.salon_name

		
'''
class User(models.Model):
	userid = 
	username = 
	nickname = 
	birthday =
	gender = 
	email = 
'''