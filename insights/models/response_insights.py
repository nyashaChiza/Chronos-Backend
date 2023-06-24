from django.db import models
from evaluation.models import Response, Participant, Evaluation

class ResponseInsights(models.Model):
    response = models.OneToOneField(Response, on_delete=models.CASCADE)
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    evaluation = models.OneToOneField(Evaluation, on_delete=models.CASCADE)
    response_length = models.IntegerField()