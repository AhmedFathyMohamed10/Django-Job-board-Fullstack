from django.urls import path
from . import views

# Api views
from . import api_views

urlpatterns = [
	path('', views.job_list, name='all-jobs'),
	path('add-job/', views.add_job, name='add-job'),
	path('<str:slug>/', views.job_details, name='job-details'),
    
	# APIs
	path('api/list', api_views.JobListApi.as_view(), name='api-jobs'),
	path('api/create', api_views.JobCreateApi.as_view(), name='api-create-job'),
	path('api/<str:slug>', api_views.JobDetailList.as_view(), name='api-details-job'),
	path('api/<str:slug>/update', api_views.JobDetailUpdate.as_view(), name='api-details-job-update'),
	path('api/<str:slug>/delete', api_views.JobDelete.as_view(), name='api-details-job-delete'),
]