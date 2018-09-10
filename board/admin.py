from django.contrib import admin

from .models import ComputerBoard


@admin.register(ComputerBoard)
class ComputerBoard(admin.ModelAdmin):
	list_display = ['id', 'title', 'nickname', 'hit', 'updated', 'created']