from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from insights.helpers import InsightsCalculator

class Participant(models.Model):
    GENDER_CHOICES=(
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Other" )
    evaluation = models.ForeignKey('evaluation.Evaluation', on_delete= models.SET_NULL ,related_name="participants", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    
    
    