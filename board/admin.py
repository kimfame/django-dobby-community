from django.contrib import admin

from .models import Board


@admin.register(Board)
class Board(admin.ModelAdmin):
	list_display = ['id', 'title', 'nickname', 'hit', 'updated', 'created']