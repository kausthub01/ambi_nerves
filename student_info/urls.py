from django.urls import path
from . import views
   # optional, but useful for namespacing

urlpatterns = [
    path('', views.index, name='studentinfo_index'),   
    path('create/', views.create_student, name='create-student'),
    path('edit/<int:pk>/', views.edit_student, name= 'edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]