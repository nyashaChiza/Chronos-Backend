from django.db import models
from evaluation.models import Evaluation 

class EvaluationInsights(models.Model):
    evaluation = models.OneToOneField(Evaluation, on_delete=models.CASCADE)
    total_participants = models.IntegerField()
    total_questions = models.IntegerField()
    total_responses = models.IntegerField()
    average_score = models.FloatField()
    minimum_score = models.FloatField()
    maximum_score = models.FloatField()