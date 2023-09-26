from django.db import models
from django.utils import timezone


# Create your models here.
class Idea(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Mid', 'Mid'),
        ('Low', 'Low')
    ]

    title = models.CharField(max_length=100, blank=False)
    dateAdded = models.DateField(default=timezone.now())
    content = models.CharField(max_length=500, blank=True)
    priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title