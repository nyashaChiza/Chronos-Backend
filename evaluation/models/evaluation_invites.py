from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils import timezone
import uuid
from django.conf import settings

class EvaluationInvite(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    evaluation = models.ForeignKey("evaluation.Evaluation", on_delete=models.SET_NULL, related_name="evaluation_invite", null=True)
    participant = models.ForeignKey("evaluation.Participant", on_delete=models.SET_NULL, related_name="participant_invite", null=True)
    valid_for_in_minutes = models.PositiveIntegerField(default=30, validators=[MinValueValidator(1), MaxValueValidator(60)])
    is_accepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def is_valid(self):
        accepted_invites_count = EvaluationInvite.objects.filter(evaluation=self.evaluation, is_accepted=True).count()
        # Calculate the expiration time based on the creation time and valid_for_in_minutes
        expiration_time = self.created + timezone.timedelta(minutes=self.valid_for_in_minutes)
        # Compare the current time with the expiration time to check if the invite is still valid
        return timezone.now() <= expiration_time and accepted_invites_count <= self.evaluation.maximum_participants 
    
    def get_invite_accept_link(self):
        return reverse('accept-invite', kwargs={'invite_uuid': self.uuid})
    
    def save(self, *args, **kwargs):
        if not self.evaluation.is_valid():
            raise ValueError("Cannot save invite: Evaluation has ended.")
        super().save(*args, **kwargs)
    

