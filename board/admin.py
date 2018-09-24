from django.contrib import admin

from .models import Computer, Programming, Travel


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'content', 'nickname', 'hit', 'updated', 'created']

@admin.register(Programming)
class ProgrammingAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'content', 'nickname', 'hit', 'updated', 'created']

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'content', 'nickname', 'hit', 'updated', 'created']


	