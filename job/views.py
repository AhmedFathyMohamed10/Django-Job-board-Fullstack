from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def job_list(request):
	return HttpResponse('Hello Jobs')

def job_details(request, pk):
	pass	