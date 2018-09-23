from django.shortcuts import render

# models
from .models import ComputerBoard, ProgrammingBoard

# class view
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


def index(request):
	board_list = ComputerBoard.objects.order_by('-created')


	return render(request, 'board/index.html', {'board': board_list})




def getModel(db_table):
	class MyClass(models.Model):

		class Meta:
			db_table = db_table

	return MyClass

# class index(ListView):
# 	getModel

#  	def get_queryset(self):
#  		return ComputerBoard.objects.order_by('-created')












