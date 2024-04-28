from django import forms
from .models import ApplyJob, Job

class ApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = ['name', 'email', 'website_url', 'cv_file', 'cover_letter']

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'job_type', 'vacancy', 'salary', 'category', 'excperience', 'image']