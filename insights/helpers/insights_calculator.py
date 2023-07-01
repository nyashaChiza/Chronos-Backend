from django.db.models import Avg, Min, Max
from insights.models import EvaluationInsights, ParticipantInsights, QuestionInsights, ResponseInsights

class InsightsCalculator:
    @staticmethod
    def calculate_and_store_insights():
        from evaluation.models import Evaluation, Participant, Question, Response  # Import here instead

        InsightsCalculator.calculate_and_store_evaluation_insights(Evaluation, Participant, Question, Response)
        InsightsCalculator.calculate_and_store_participant_insights(Evaluation, Participant, Response)
        InsightsCalculator.calculate_and_store_question_insights(Question, Evaluation, Response)
        InsightsCalculator.calculate_and_store_response_insights(Response)

    @staticmethod
    def calculate_and_store_evaluation_insights(Evaluation, Participant, Question, Response):
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
    def calculate_and_store_participant_insights(Evaluation, Participant, Response):
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
    def calculate_and_store_question_insights(Question, Evaluation, Response):
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
    def calculate_and_store_response_insights(Response):
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