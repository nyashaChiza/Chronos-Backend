from django.db import models

class Response(models.Model):
    evaluation = models.ForeignKey("evaluation.Evaluation", on_delete=models.CASCADE)
    participant = models.ForeignKey("evaluation.Participant", on_delete=models.CASCADE)
    question = models.ForeignKey("evaluation.Question", on_delete=models.CASCADE)
    answer = models.TextField()
    is_reviewed = models.BooleanField(default=False)
    reviewer = models.ForeignKey("evaluation.Participant", on_delete=models.SET_NULL, null=True, blank=True, related_name="reviewed_responses")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Response for {self.evaluation.title} by {self.participant.name}"