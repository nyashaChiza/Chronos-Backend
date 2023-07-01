from django.db import models

class ParticipantInsights(models.Model):
    participant = models.OneToOneField("evaluation.Participant", on_delete=models.CASCADE)
    total_evaluations = models.IntegerField()
    average_response_rate = models.FloatField()
    average_score = models.FloatField()
    median_score = models.FloatField()