from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Faculty
from .forms import FacultyForm

def faculty_list(request):
    faculty_list = Faculty.objects.select_related("department").all
    return render(request,  'facultyinfo_index.html', {'facultyinfo_index': faculty_list})

def create_faculty(request):
    if request.method == 'POST':
            messages.success(request, 'Faculty created successfully!')
            return redirect('facultyinfo_index')
    else:
        form = FacultyForm()
        print('form', form)
    return render(request, 'create_faculty.html', {'form': form})


def edit_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk =pk)
    if request.method == 'POST':
        form = FacultyForm(request.post, instance=faculty)
        if form.is_valid():
            form.save()
            messages.success(request,'Faculty updated successfully!')
            return redirect('faculty_index')                
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'edit_faculty.html', {'form': form})

def delete_faculty(request,pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    faculty.delete()
    messages.success(request, 'Faculty deleted successfully!')
    return redirect('faculty_index')
