from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from insights.helpers import InsightsCalculator

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        InsightsCalculator.calculate_and_store_evaluation_insights()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        InsightsCalculator.calculate_and_store_evaluation_insights()
    
    
    