from django.shortcuts import render,redirect
from .models import Student  
from .forms import StudentForm


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
        print('request', request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentinfo_index')
        
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

