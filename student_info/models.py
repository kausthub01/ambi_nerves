from django.db import models

# Create your models here.
class Student(models.Model):
    ID = models.CharField(max_length=10)
    FirstName = models.CharField(max_length=300)
    LastName = models.CharField(max_length = 300)
    Email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    course = models. CharField(max_length = 400)
    startdate = models. DateField()
    enddate = models. DateField()
    Address = models. TextField()
    Isactive = models. BooleanField(default=True)


    def __str__(self):
        return self.FirstName + " " + self.LastName