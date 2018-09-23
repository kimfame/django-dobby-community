from django.contrib import admin

from .models import ComputerBoard, ProgrammingBoard, TravelBoard


@admin.register(ComputerBoard)
class ComputerBoardAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'nickname', 'hit', 'updated', 'created']

@admin.register(ProgrammingBoard)
class ProgrammingBoardAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'nickname', 'hit', 'updated', 'created']

@admin.register(TravelBoard)
class TravelBoardAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'nickname', 'hit', 'updated', 'created']