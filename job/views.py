from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from .models import Job
from .forms import ApplyForm, AddJobForm

# Create your views here.
def job_list(request):
	jobs = Job.objects.all()
	paginator = Paginator(jobs, 5)
	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)
	counting_jobs = jobs.count()
	context = {'jobs': page_obj, 'count': counting_jobs}
	return render(request, 'jobs.html', context)

def job_details(request, slug):
	job = get_object_or_404(Job, slug=slug)
	job_responsibilities = job.responsibility
	# Applying for the job
	if request.method == 'POST':
		form = ApplyForm(request.POST, request.FILES)
		if form.is_valid():
			# Save the form data and associate it with the job
			application = form.save(commit=False)
			application.job = job
			application.save()
			return redirect('all-jobs')
	else:
		form = ApplyForm() 
	context = {'job': job, 'form': form, 'job_responsibilities': job_responsibilities}
	return render(request, 'job_details.html', context)

@login_required
def add_job(request):
	if request.method == 'POST':
		form = AddJobForm(request.POST, request.FILES)
		if form.is_valid():
			adding = form.save(commit=False)
			adding.owner = request.user
			adding.save()
			return redirect('all-jobs')
	else:
		form = AddJobForm()
	return render(request, 'add_job.html', {'form': form})


