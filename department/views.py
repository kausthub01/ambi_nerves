from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Department
from .forms import DepartmentForm

def department_list(request):
    department_list= Department.objects.all()
    return render(request, 'department_index.html', {'department_index': department_list})

def create_department(request):
    if request.method == 'POST':
        messages.success(request, 'Department created successfully')
        return redirect('department_index')
    else:
        form = DepartmentForm()
    return render(request, 'create_department.html', {'form': form})


def edit_department(request, pk):
    Department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form =  DepartmentForm(request.post, instance=Department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department updated successfully')
            return redirect('department_index')
        
    else:
        form = DepartmentForm(instace = Department)
    return render(request, 'edit_courses.html', {'form' : form})


def delete_department(request, pk):
    department = get_object_or_404(department, pk=pk)
    department.delete()
    messages.success(request, 'department deleted successfully!')
    return redirect('department_index')

# Create your views here.























