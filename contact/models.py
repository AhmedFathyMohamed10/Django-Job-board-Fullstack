from django.db import models

# Create your models here.
class Info(models.Model):
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Informations'

    def __str__(self) -> str:
        return self.email