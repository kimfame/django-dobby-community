from django.db import models
from django.conf import settings
from django.utils import timezone

# add fields in User Model
# class User(models.Model):
# 	userid = 
# 	username = 
# 	nickname = 
# 	birthday =
# 	gender = 
# 	email =  

class BaseBoard(models.Model):
	class Meta:
		abstract = True	

	title = models.CharField(max_length=200)
	content = models.TextField()
	nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
	hit = models.PositiveIntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class Computer(BaseBoard):
	pass

class Programming(BaseBoard):
	pass

class Travel(BaseBoard):
	pass