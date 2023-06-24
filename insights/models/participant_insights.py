from django.db import models
from evaluation.models import Participant

class ParticipantInsights(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    total_evaluations = models.IntegerField()
    average_response_rate = models.FloatField()
    average_score = models.FloatField()
    median_score = models.FloatField()