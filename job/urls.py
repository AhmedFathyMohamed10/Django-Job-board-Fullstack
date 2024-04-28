from django.urls import path
from . import views

urlpatterns = [
	path('', views.job_list, name='all-jobs'),
	path('add-job/', views.add_job, name='add-job'),
	path('<str:slug>/', views.job_details, name='job-details'),
]