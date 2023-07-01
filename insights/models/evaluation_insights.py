from django.db import models
# from evaluation.models import Evaluation 

class EvaluationInsights(models.Model):
    evaluation = models.OneToOneField("evaluation.Evaluation", on_delete=models.CASCADE)
    average_score = models.FloatField()
    minimum_score = models.FloatField()
    maximum_score = models.FloatField()
    
    def completion_rate(self):
        return  (self.evaluation.number_of_responses / self.evaluation.number_of_participants) * 100