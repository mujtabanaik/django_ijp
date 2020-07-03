from django.db import models
import datetime

loc = (('Bangalore', 'Bangalore'), ('Noida', 'Noida'))
division = (('SP & T', 'SP & T'), ('Managed Services', 'Managed Services'),('Managed Services', 'Managed Services'))
stat = (('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Joined', 'Joined'))


class JobRequirement(models.Model):
    request_id = models.CharField(max_length=10)
    division = models.CharField(max_length=30, choices=division)
    experience = models.IntegerField()
    designation = models.CharField(max_length=50)
    date_posted = models.DateField()
    date_expiry = models.DateField()
    location = models.CharField(max_length=20, choices=loc)
    skills = models.CharField(max_length=500)
    job_description = models.TextField()

    def __str__(self):
        return f"{self.request_id}"


class JobApplicant(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=15)
    current_level = models.IntegerField()
    current_designation = models.CharField(max_length=50)
    current_division = models.CharField(max_length=20, choices=division)
    skills = models.CharField(max_length=500)
    reporting_manager = models.CharField(max_length=100)
    reporting_lead = models.CharField(max_length=100)
    current_project = models.CharField(max_length=200)
    duration_in_current_Level = models.FloatField(max_length=20)
    last_promotion_if_any_and_when = models.CharField(max_length=300)
    job_id = models.ForeignKey(JobRequirement, on_delete=models.CASCADE)
    date_applied = models.DateField()
    status = models.CharField(max_length=20, choices=stat)

    def __str__(self):
        return f"{self.employee_name} applied to job {self.job_id} on {self.date_applied}"


