from django.db import models


class ResponseInsights(models.Model):
    response = models.OneToOneField("evaluation.Response", on_delete=models.CASCADE)
    participant = models.OneToOneField("evaluation.Participant", on_delete=models.CASCADE)
    evaluation = models.OneToOneField("evaluation.Evaluation", on_delete=models.CASCADE)
    response_length = models.IntegerField()