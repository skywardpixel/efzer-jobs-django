from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Job(models.Model):
    published = models.BooleanField(default=True)
    date_published = models.DateTimeField(default=timezone.now)
    times_viewed = models.IntegerField(default=0)

    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    job_position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)

    submitting_resume = models.CharField(max_length=300)

    description = models.CharField(max_length=300, blank=True)
    requirements = models.CharField(max_length=300, blank=True)
    company_description = models.CharField(max_length=2000, blank=True)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.job_position + " at " + self.department + ", " + self.company + " in " + self.location

    def get_absolute_url(self):
        return reverse('jobs:detail', kwargs={'pk': self.pk})