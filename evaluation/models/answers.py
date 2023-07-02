from django.db import models
from evaluation.models import Question, Response
from django.core.validators import MinValueValidator, MaxValueValidator


class Answer(models.Model):
    RESPONSE_TYPES = [
        ('text', 'Text'),
        ('checkbox', 'Checkbox'),
        ('radio', 'Radio Button'),
    ]

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.TextField(null=True,blank=True)
    response_type = models.CharField(max_length=10, choices=RESPONSE_TYPES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_selected = models.BooleanField(default=False)
    weight = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.answer_text


    def save(self, *args, **kwargs):
        if not self.question.evaluation.is_valid():
            raise ValueError("Cannot save answer: Evaluation has ended.")
        super().save(*args, **kwargs)