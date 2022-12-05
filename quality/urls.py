"""servicePlan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from quality import views


urlpatterns = [
    path('', views.main, name='main'),
    path('project/input/', views.project_input, name='project_input'),
    path('project/list/', views.project_list, name='project_list'),
    path('project/deatil/<int:pk>/', views.project_detail, name='project_detail'),


    path('scenario/update/<int:pk>/', views.scenario_update, name='scenario_update'),
    # path('scenario/list/', views.scenario_input, name='scenario_list'),
    path('scenario/deatil/<int:pk>/', views.scenario_detail, name='scenario_detail'),
    path('scenario/deatil/<int:pk0>/<int:pk1>/', views.scenario_detail_block, name='scenario_detail_block'),

    path('block/input/', views.block_input, name='block_input'),
    path('block/list/', views.block_list, name='block_list'),
    path('block/update/<int:pk0>/<int:pk1>/', views.block_update, name='block_update'),

    path('comment/input/<int:pk0>/<int:pk1>/<int:pk2>/', views.comment_input, name='comment_input'),
    path('comment/list/', views.comment_input, name='comment_list'),

    path('confirm/<int:pk0>/<int:pk1>/', views.confirm, name='confirm')
]

