from django.db import models



# Create your models here.
class Job(models.Model):

	JOB_TYPE_CHOICES = (
		('FULL TIME', 'Full Time'),
		('PART TIME', 'Part Time')
	)

	title = models.CharField(max_length=200)
	description = models.TextField()
	job_type = models.CharField(max_length=100, choices=JOB_TYPE_CHOICES)
	# location = models.CharField(max_length=200)
	vacancy = models.IntegerField(default=1)
	salary = models.IntegerField(default=0)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	excperience = models.IntegerField(default=1)
	published_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
