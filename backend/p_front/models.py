from django.db import models
from django.utils import timezone

# Creating works listing

class Works(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    role = models.CharField(max_length=255, null=True, blank=False)
    year = models.DateTimeField()
    client = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='media/works/', null=True, blank=True)

    def __str__(self):
        return self.title
