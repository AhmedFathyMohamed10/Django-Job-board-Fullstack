from django.urls import path
from . import views

urlpatterns = [
	path('', views.job_list, name='all-jobs'),
	path('<str:pk>/', views.job_details, name='job-details'),
]