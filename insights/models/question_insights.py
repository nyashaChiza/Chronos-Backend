from django.db import models


class QuestionInsights(models.Model):
    question = models.OneToOneField("evaluation.Question", on_delete=models.CASCADE)
    total_responses = models.IntegerField()
    response_rate = models.FloatField()
    average_score = models.FloatField()
    median_score = models.FloatField()