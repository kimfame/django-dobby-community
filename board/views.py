from django.shortcuts import render

# models
from django.db import models
from .models import BaseBoard, Computer, Programming, Travel

# class view
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


### example function based view
# def index(request):
# 	board_list = ComputerBoard.objects.order_by('-created')
# 	return render(request, 'board/index.html', {'board': board_list})


### example class based view
# class index(ListView):
# 	model = ProgrammingBoard

# 	context_object_name = 'board'

# 	template_name = 'board/index.html'

# 	def get_queryset(self):
#  		return ProgrammingBoard.objects.order_by('-created')


################################# method 1
# def getModel(db_table_name):
# 	class MyClassMetaclass(models.base.ModelBase):
# 		def __new__(cls, name, bases, attrs):
# 		  	name += db_table
# 		  	return models.base.ModelBase.__new__(cls, name, bases, attrs)

# 	class MyClass(BaseBoard):
# 		__metaclass__ = MyClassMetaclass

# 		class Meta:
# 			db_table = db_table_name

# 	return MyClass

################################ method 2
def getModel(db_table_name):
	class BoardClass(BaseBoard):

		class Meta:
			db_table = db_table_name

	return BoardClass

##################################### class 
# class TableController():

# 	def __init__(self):
# 		self.tables = ["computer", "programming", "travel"]
# 		self.table_map = {}

# 		for table in self.tables:
# 			print("================ " + table)
# 			class BoardClass(BaseBoard):
# 				db_table = "board_" + table

# 			self.table_map[table] = BoardClass

# 	def getModel(self, db_table_name):
# 		return self.table_map[db_table_name]


# xxx = TableController()


################################# global
# tables = ["computer", "programming", "travel"]
# table_map = {}

# for table in tables:
# 	print("================ " + table)
# 	class BoardClass(BaseBoard):

# 		class Meta:
# 			db_table = "board_" + table

# 	table_map[table] = BoardClass



class index(ListView):
	#model = getModel("board_travel")

	context_object_name = 'list'

	template_name = 'board/index.html'

	def get_queryset(self):
		return getModel("travel").objects.all()
 









