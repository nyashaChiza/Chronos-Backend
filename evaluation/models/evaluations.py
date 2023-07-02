from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# from insights.helpers import InsightsCalculator
import uuid

from django.urls import reverse

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
    
    def number_of_evaluations(self):
        return self.evaluations.count()

class Attachment(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='attachments/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.name}"

class Evaluation(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    maximum_score = models.PositiveIntegerField(null=True, blank=True)
    maximum_participants = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', null=True, blank=True, related_name="evaluations")
    attachments = models.ManyToManyField('Attachment', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def age_distribution(self):
        age_distribution = {f"{range_start} - {range_start + 9}": 0 for range_start in range(18, 73, 10)}
        
        for participant in self.participants.all():
            if participant.date_of_birth:
                age = self._calculate_age(participant.date_of_birth)
                for age_range in age_distribution:
                    range_start, range_end = map(int, age_range.split(" - "))
                    if age >= range_start and age <= range_end:
                        age_distribution[age_range] += 1
        
        return age_distribution
    
    def gender_distribution(self):
        gender_distribution = {
            "Male": 0,
            "Female": 0,
            "Other": 0
        }
        
        for participant in self.participants.all():
            gender = participant.gender
            gender_distribution[gender] += 1
        
        return gender_distribution
    
    def _calculate_age(self, birth_date):
        today = date.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age

    def __str__(self):
        return self.title
    
    def number_of_participants(self):
        return self.participants.count()
    
    def number_of_responses(self):
        return self.response_evaluation.count()
    
    def get_invite_link(self):
        url =  "api/v1/participants/create/" # Replace 'create-participant' with your actual endpoint name
        return f"{url}?ev={self.uuid}"