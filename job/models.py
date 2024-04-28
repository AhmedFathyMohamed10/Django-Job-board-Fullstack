from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Customize the image uploading to the media folder
def helper_upload_image(instance, file_name):
    _, extension = file_name.split(".")
    return "jobs/{}.{}".format(instance.title, extension)

class Job(models.Model):

	JOB_TYPE_CHOICES = (
		('Full Time', 'Full Time'),
		('Part Time', 'Part Time')
	)
	owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField()
	job_type = models.CharField(max_length=100, choices=JOB_TYPE_CHOICES)
	# location = models.CharField(max_length=200)
	vacancy = models.IntegerField(default=1)
	salary = models.IntegerField(default=0)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	excperience = models.IntegerField(default=1)
	image = models.ImageField(upload_to=helper_upload_image)
	published_at = models.DateTimeField(auto_now_add=True)

	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if ' ' in self.title:
			title = self.title
			title = title.replace(' ', '-')
			self.slug = title.lower()
		super(Job, self).save(*args, **kwargs)


	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

from datetime import datetime
class ApplyJob(models.Model):
	job = models.ForeignKey(Job, related_name='applies', on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	website_url = models.URLField()
	cv_file = models.FileField(upload_to='jobs/CVs/')
	cover_letter = models.TextField()

	def __str__(self) -> str:
		return self.email