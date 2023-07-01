from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from insights.helpers import InsightsCalculator


class Question(models.Model):
    evaluation = models.ForeignKey("evaluation.Evaluation", on_delete=models.CASCADE)
    text = models.TextField()
    order = models.PositiveIntegerField()
    is_required = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # InsightsCalculator.calculate_and_store_evaluation_insights()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # InsightsCalculator.calculate_and_store_evaluation_insights()
        
    def number_of_answers(self):
        return self.answers.count()