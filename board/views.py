#from django.shortcuts import render

from django.urls import reverse_lazy

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
# def get_model(db_table_name):
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
# def get_model(db_table_name):
# 	class BoardClass(BaseBoard):

# 		class Meta:
# 			db_table = db_table_name

# 	return BoardClass


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
tables = ["computer", "programming", "travel"]
table_map = {}
print("*********************************** GLOBAL")

for table in tables:
	print("===> " + table)
	class BoardClass(BaseBoard):

		class Meta:
			db_table = "board_" + table

	table_map[table] = BoardClass

def get_model(db_table_name):
	global table_map
	return table_map[db_table_name]



def get_start_and_end_index(max_index, current_index, page_range_displayed):
	
	# 원소가 표현할 개수 이하일 때
	if max_index <= page_range_displayed:
		start_index = 0
		end_index = max_index
	
	# 원소가 표현할 개수 이상이면서 현재 위치가 첫 페이지 그룹에 위치할 때
	elif max_index > page_range_displayed and current_index <= int(page_range_displayed / 2):
		start_index = 0
		end_index = page_range_displayed

	# 원소가 표현할 개수 이상이면서 현재 위치가 마지막 페이지 그룹에 위치할 때
	elif max_index > page_range_displayed and current_index >= max_index - int(page_range_displayed / 2): 
		start_index = max_index - page_range_displayed
		end_index = max_index
	
	# 현재 페이지 위치가 중간에 위치할 때
	else:
		if(page_range_displayed % 2 == 1):
			start_index = current_index - int(page_range_displayed / 2)
			end_index = current_index + int(page_range_displayed / 2) + 1
		else:
			start_index = current_index - int(page_range_displayed / 2)
			end_index = current_index + int(page_range_displayed / 2)
	return (start_index, end_index)



class List(ListView):
	# 20-30
	paginate_by = 3
	context_object_name = 'list'
	template_name = 'board/list.html'
	
	def get_queryset(self):
		board_name = self.kwargs['board_name']		
		return get_model(board_name).objects.order_by('-created')
 
	def get_context_data(self, **kwargs):
		context = super(List, self).get_context_data(**kwargs)
		
		paginator = context['paginator']

		try:
			page = self.request.GET.get('page')
			current_page = paginator.page(page)
		except:
			current_page = paginator.page(1)

		# current index
		current_index = current_page.number - 1

		print("current_index : " + str(current_index))

		# last index
		max_index = len(paginator.page_range)

		print("max_index : " + str(max_index))

		# display number of pages
		page_range_displayed = 5

		# calculate start and end index
		result_index = get_start_and_end_index(max_index, current_index, page_range_displayed)

		print("result_index[0] : " + str(result_index[0]))
		print("result_index[1] : " + str(result_index[1]))

		page_range = paginator.page_range[result_index[0]:result_index[1]]

		context['page_range'] = page_range

		return context


class Read(DetailView):
	context_object_name = 'read'
	template_name = 'board/read.html'

	def get_queryset(self):
		board_name = self.kwargs['board_name']
		return get_model(board_name).objects.filter(id=self.kwargs['pk'])


class Create(CreateView):
	fields = ['title', 'content']
	template_name = 'board/form.html'

	def get_queryset(self):
		board_name = self.kwargs['board_name']
		return get_model(board_name).objects.none()

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.nickname = self.request.user
		obj.save()
		return super(Create, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('board:read', args=(self.kwargs['board_name'], self.object.id))


class Update(UpdateView):
	fields = ['title', 'content']
	template_name = 'board/form.html'

	def get_queryset(self):
		board_name = self.kwargs['board_name']
		return get_model(board_name).objects.filter(id=self.kwargs['pk'])

	def get_success_url(self):
		return reverse_lazy('board:read', args=(self.kwargs['board_name'], self.object.id))









