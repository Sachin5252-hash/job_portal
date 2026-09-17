from django import forms

from .models import Company, Job


class Jobform(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location', 'salary', 'notice_period']
        labels = {'company': 'Company'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].empty_label = 'Select a company'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'location', 'website', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }