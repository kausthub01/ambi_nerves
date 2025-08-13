from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Courses
from .forms import CoursesForm

def courses_list(request):
    courses_list= Courses.objects.all()
    return render(request, 'courses_index.html', {'courses_index': courses_list})

def create_courses(request):
    if request.method == 'POST':
        messages.success(request, 'Course created successfully')
        return redirect('courses_index')
    else:
        form = CoursesForm()
    return render(request, 'create_courses.html', {'form': form})


def edit_courses(request, pk):
    courses = get_object_or_404(Courses, pk=pk)
    if request.method == 'POST':
        form =  CoursesForm(request.post, instance=courses)
        if form.is_valid():
            form.save()
            messages.success(request, 'Courses updated successfully')
            return redirect('courses_index')
        
    else:
        form = CoursesForm(instace = courses)
    return render(request, 'edit_courses.html', {'form' : form})


def delete_faculty(request, pk):
    courses = get_object_or_404(Courses, pk=pk)
    courses.delete()
    messages.success(request, 'Course deleted successfully!')
    return redirect('courses_index')
# Create your views here.
