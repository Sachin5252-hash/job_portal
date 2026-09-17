from django.conf import settings
from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey('Company', on_delete=models.PROTECT, related_name='jobs',default=0)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    notice_period = models.CharField(max_length=100, blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

class Company(models.Model):
    company_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['company_name']

    def __str__(self):
        return self.company_name

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_applied = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['job', 'applicant']

    def __str__(self):
        return f"{self.applicant} applied to {self.job}"
