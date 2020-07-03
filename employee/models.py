from django.db import models
from django.contrib.auth.models import User
from enum import Enum

emp_type = (('Permanent', 'Permanent'), ('Contract', 'Contract'))
emp_status = (('Active', 'Active'), ('Inactive', 'Inactive'))
sex = (("Male", "Male"), ("Female", "Female"))
status = (('Single', 'Single'), ('Married', 'Married'), ('Other', 'Other'))


class Employee(models.Model):
    emp = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    cu_id = models.CharField(max_length=10)
    dob = models.DateField()
    designation = models.CharField(max_length=100)
    employee_type = models.CharField(max_length=20, choices=emp_type)
    emp_level = models.IntegerField()
    employee_status = models.CharField(max_length=10, choices=emp_status)
    contact = models.CharField(max_length=12)
    joining_date = models.DateField()
    skill_set = models.TextField()
    gender = models.CharField(max_length=10, choices=sex)
    address = models.TextField()
    marital_status = models.CharField(max_length=10, choices=status)

    def __str__(self):
        return self.name


