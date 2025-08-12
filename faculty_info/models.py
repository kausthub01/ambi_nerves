from django.db import models

class Department(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Faculty(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField(unique=True)
    phone       = models.CharField(max_length=20, blank=True)
    department  = models.ForeignKey(Department, on_delete=models.PROTECT)
    title       = models.CharField(max_length=100, blank=True)
    hire_date   = models.DateField(null=True, blank=True)
    end_date    = models.DateField(null=True, blank=True)
    office_room = models.CharField(max_length=50, blank=True)
    address     = models.TextField(blank=True)
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"


