from django import forms
from .models import Department, Faculty


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        
        fields = ["employee_id", "first_name", "last_name",
            "email", "phone", "department", "hire_date", "end_date",
            "office_room", "address", "is_active",
        ]


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["code", "name"]
        