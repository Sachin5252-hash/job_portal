from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CompanyForm, Jobform
from .models import Application, Company, Job


class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'all_jobs'

    def get_queryset(self):
        sort = self.request.GET.get('sort', '-date_posted')
        sortable_fields = {
            'title': 'title',
            'company_name': 'company__company_name',
            'location': 'location',
            'salary': 'salary',
            'notice_period': 'notice_period',
            'date_posted': 'date_posted',
        }
        descending = sort.startswith('-')
        field_name = sortable_fields.get(sort.lstrip('-'))
        if field_name is None:
            sort = '-date_posted'
        else:
            sort = f'-{field_name}' if descending else field_name
        return Job.objects.select_related('company').order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', '-date_posted')
        return context


class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['already_applied'] = Application.objects.filter(
                job=self.object, applicant=self.request.user
            ).exists()
        return context


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = Jobform
    template_name = 'job_form.html'

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('job-detail', kwargs={'pk': self.object.pk})


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = Jobform
    template_name = 'job_form.html'

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user)

    def get_success_url(self):
        return reverse('job-detail', kwargs={'pk': self.object.pk})


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = 'job_confirm_delete.html'
    success_url = reverse_lazy('my-jobs')

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user)

class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'
    context_object_name = 'companies'

    def get_queryset(self):
        return Company.objects.select_related('created_by')


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('company-list')


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_form.html'

    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user)

    def get_success_url(self):
        return reverse('company-list')


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'company_confirm_delete.html'
    success_url = reverse_lazy('company-list')

    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user)


class MyJobsListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'my_jobs_list.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user)


@login_required
def apply_to_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    application, created = Application.objects.get_or_create(job=job, applicant=request.user)
    if created:
        messages.success(request, f'You applied to "{job.title}".')
    else:
        messages.info(request, 'You have already applied to this job.')
    return redirect('job-detail', pk=job.pk)


class MyApplicationsListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'my_applications_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).select_related('job', 'job__company')
