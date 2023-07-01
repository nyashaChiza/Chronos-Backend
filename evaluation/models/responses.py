from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from insights.helpers import InsightsCalculator

class Response(models.Model):
    evaluation = models.ForeignKey("evaluation.Evaluation", on_delete=models.CASCADE,related_name="response_evaluation")
    participant = models.ForeignKey("evaluation.Participant", on_delete=models.CASCADE,related_name="response_participant")
    question = models.ForeignKey("evaluation.Question", on_delete=models.CASCADE,related_name="response_question")
    answer = models.ForeignKey("evaluation.Answer", on_delete=models.CASCADE, related_name="response_answer")
    is_reviewed = models.BooleanField(default=False)
    reviewer = models.ForeignKey("evaluation.Participant", on_delete=models.SET_NULL, null=True, blank=True, related_name="reviewed_responses")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Response for {self.evaluation.title} by {self.participant.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # InsightsCalculator.calculate_and_store_evaluation_insights()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # InsightsCalculator.calculate_and_store_evaluation_insights()