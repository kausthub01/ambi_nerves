from django.urls import path
from .views import *


urlpatterns= [
    path ('', faculty_list, name='facultyinfo_index'),
    path ('create/', create_faculty, name='create_faculty'),
    path ('edit/<int:pk>/', edit_faculty, name='edit_faculty'),
    path('delete/<int:pk>/', delete_faculty, name='delete_faculty'),
]

