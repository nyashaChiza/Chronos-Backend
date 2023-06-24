from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from insights.helpers import InsightsCalculator

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('archived', 'Archived'),
)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Attachment(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='attachments/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    maximum_score = models.PositiveIntegerField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    attachments = models.ManyToManyField('Attachment', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        InsightsCalculator.calculate_and_store_evaluation_insights()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        InsightsCalculator.calculate_and_store_evaluation_insights()

    def __str__(self):
        return self.title