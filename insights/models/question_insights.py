from django.db import models
from evaluation.models import Question

class QuestionInsights(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    total_responses = models.IntegerField()
    response_rate = models.FloatField()
    average_score = models.FloatField()
    median_score = models.FloatField()