from django.db import models
from django.conf import settings
from django.utils import timezone

from ckeditor.fields import RichTextField

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
	content = RichTextField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
	hit = models.PositiveIntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title



'''
class BaseComment(models.Model):
	class Meta:
		abstract = True
		
	comment = models.CharField(max_length=256)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
	parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
	sequence = models.PositiveIntegerField(default=1)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.comment

class ComputerComment(BaseComment):
	group = models.ForeignKey('Computer', on_delete=models.DO_NOTHING)
	
class ProgrammingComment(BaseComment):
	group = models.ForeignKey('Porgramming', on_delete=models.DO_NOTHING)

class TravelComment(BaseComment):
	group = models.ForeignKey('Travel', on_delete=models.DO_NOTHING)
'''

class Computer(BaseBoard):
	pass

class Programming(BaseBoard):
	pass

class Travel(BaseBoard):
	pass