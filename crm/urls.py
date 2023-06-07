from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.index, name='index'),
    path('', views.home, name='home'),
    # path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('record/<int:pk>', views.records, name='record'),
    path('delete/<int:pk>', views.delete_cst, name='delete'),
    path('add/', views.add_cst, name='add'),
    path('update/<int:pk>', views.update_cst, name='update')

]
