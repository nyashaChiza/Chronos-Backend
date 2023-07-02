from evaluation.models import Evaluation
from django.core.mail import send_mail
from django.conf import settings

def send_event_reminders():
    evaluations = Evaluation.objects.all()

    for evaluation in evaluations:
        if evaluation.send_reminder():
            for participant in evaluation.participants.all():
                subject = f"Reminder: Evaluation {evaluation.title} starts soon"
                message = f"Dear {participant.name}, this is a reminder that the evaluation for {evaluation.title} will start soon at {evaluation.start_date} and end at {evaluation.end_date}. Please make sure to be prepared."

                # Send the reminder email
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [participant.email])
                settings.LOGGER(f'evaluation reminder for {evaluation} sent to {participant}')