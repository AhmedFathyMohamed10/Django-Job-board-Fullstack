from django.shortcuts import render, get_object_or_404


from .models import Job

# Create your views here.
def job_list(request):
	jobs = Job.objects.all()
	context = {'jobs': jobs}
	return render(request, 'jobs.html', context)

def job_details(request, pk):
	job = get_object_or_404(Job, id=pk)
	context = {'job': job}
	return render(request, 'job_details.html', context)