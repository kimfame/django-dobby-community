"""dobby URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
	#path('', views.index, name='index'),
	#path('', views.index.as_view(), name='index'),
	
    path('<slug:board_name>/list', views.List.as_view(), name='list'),
    ########## temp
    path('<slug:board_name>', views.List.as_view(), name='list'),
    
    path('<slug:board_name>/read/<int:pk>', views.Read.as_view(), name='read'),
    path('<slug:board_name>/create', views.Create.as_view(), name='create'),
    path('<slug:board_name>/update/<int:pk>', views.Update.as_view(), name='update'),
    path('<slug:board_name>/delete/<int:pk>', views.Delete.as_view(), name='delete'),

]