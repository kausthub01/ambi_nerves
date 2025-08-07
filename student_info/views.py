from django.shortcuts import render,redirect
from .models import Student  
from .forms import StudentForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.


def index(request):
    print(" index view called")
    students = Student.objects.all()  # ✅ Get all student records from the DB
    print("Students fetched:", students)
    return render(request, 'studentinfo_index.html',{'studentslist': students})


def create_student(request):
    print('request', request.method)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print('Form data', request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Student created successfully!')
            return redirect('studentinfo_index')
        
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('studentinfo_index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request,pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, 'Student deleted successfully!')
    return redirect('studentinfo_index')

                   
                  
