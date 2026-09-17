from django.contrib import admin

from .models import Application, Company, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'salary', 'posted_by', 'date_posted']
    search_fields = ['title', 'company__company_name']
    list_filter = ['location']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'date_applied']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'location', 'website', 'created_by', 'created_at']
    search_fields = ['company_name', 'location']
