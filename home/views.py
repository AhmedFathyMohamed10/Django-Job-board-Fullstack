from django.shortcuts import render
from job.models import Job
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    
    counting_jobs = jobs.count()
    context = {'jobs': jobs, 'count': counting_jobs}
    return render(request, 'home.html', context)