from django import forms
from .models import Courses

class coursesform(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'















