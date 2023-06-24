from django.db import models
from django.db.models import Avg, Min, Max
from insights.models import EvaluationInsights, ParticipantInsights, QuestionInsights, ResponseInsights
from evaluation.models import Evaluation, Participant, Question, Response

class InsightsCalculator:
    @staticmethod
    def calculate_and_store_insights():
        InsightsCalculator.calculate_and_store_evaluation_insights()
        InsightsCalculator.calculate_and_store_participant_insights()
        InsightsCalculator.calculate_and_store_question_insights()
        InsightsCalculator.calculate_and_store_response_insights()

    @staticmethod
    def calculate_and_store_evaluation_insights():
        evaluations = Evaluation.objects.all()
        for evaluation in evaluations:
            total_participants = Participant.objects.filter(evaluations=evaluation).count()
            total_questions = Question.objects.filter(evaluation=evaluation).count()
            total_responses = Response.objects.filter(evaluation=evaluation).count()
            average_score = Response.objects.filter(evaluation=evaluation).aggregate(avg_score=Avg('score'))['avg_score']
            minimum_score = Response.objects.filter(evaluation=evaluation).aggregate(min_score=Min('score'))['min_score']
            maximum_score = Response.objects.filter(evaluation=evaluation).aggregate(max_score=Max('score'))['max_score']

            EvaluationInsights.objects.update_or_create(
                evaluation=evaluation,
                defaults={
                    'total_participants': total_participants,
                    'total_questions': total_questions,
                    'total_responses': total_responses,
                    'average_score': average_score,
                    'minimum_score': minimum_score,
                    'maximum_score': maximum_score
                }
            )

    @staticmethod
    def calculate_and_store_participant_insights():
        participants = Participant.objects.all()
        for participant in participants:
            total_evaluations = Evaluation.objects.filter(participants=participant).count()
            average_score = Response.objects.filter(participant=participant).aggregate(avg_score=Avg('score'))['avg_score']
            median_score = Response.objects.filter(participant=participant).aggregate(median_score=Avg('score'))['median_score']

            ParticipantInsights.objects.update_or_create(
                participant=participant,
                defaults={
                    'total_evaluations': total_evaluations,
                    'average_score': average_score,
                    'median_score': median_score
                }
            )

    @staticmethod
    def calculate_and_store_question_insights():
        questions = Question.objects.all()
        total_evaluations = Evaluation.objects.count()
        for question in questions:
            total_responses = Response.objects.filter(question=question).count()
            average_score = Response.objects.filter(question=question).aggregate(avg_score=Avg('score'))['avg_score']
            median_score = Response.objects.filter(question=question).aggregate(median_score=Avg('score'))['median_score']

            QuestionInsights.objects.update_or_create(
                question=question,
                defaults={
                    'total_responses': total_responses,
                    'average_score': average_score,
                    'median_score': median_score
                }
            )

    @staticmethod
    def calculate_and_store_response_insights():
        responses = Response.objects.all()
        for response in responses:
            participant = response.participant
            evaluation = response.evaluation
            response_length = len(response.text)

            ResponseInsights.objects.update_or_create(
                response=response,
                defaults={
                    'participant': participant,
                    'evaluation': evaluation,
                    'response_length': response_length
                }
            )
