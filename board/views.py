from django.shortcuts import render

# models
from .models import ComputerBoard, ProgrammingBoard

# class view
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView



class index(ListView):
		


	def get_queryset(self):

		return ComputerBoard.objects.order_by('-created')












