from django.contrib import admin

# Register your models here.
from django.contrib import admin
from insights.models import EvaluationInsights, ParticipantInsights, QuestionInsights, ResponseInsights

@admin.register(EvaluationInsights)
class EvaluationInsightsAdmin(admin.ModelAdmin):
    list_display = ('evaluation', 'total_participants', 'total_questions', 'total_responses', 'average_score', 'minimum_score', 'maximum_score')
    list_filter = ('evaluation',)
    search_fields = ('evaluation__name',)

@admin.register(ParticipantInsights)
class ParticipantInsightsAdmin(admin.ModelAdmin):
    list_display = ('participant', 'total_evaluations', 'average_response_rate', 'average_score', 'median_score')
    list_filter = ('participant',)
    search_fields = ('participant__name',)

@admin.register(QuestionInsights)
class QuestionInsightsAdmin(admin.ModelAdmin):
    list_display = ('question', 'total_responses', 'response_rate', 'average_score', 'median_score')
    list_filter = ('question',)
    search_fields = ('question__text',)

@admin.register(ResponseInsights)
class ResponseInsightsAdmin(admin.ModelAdmin):
    list_display = ('response', 'participant', 'evaluation', 'response_length')
    list_filter = ('participant', 'evaluation')
    search_fields = ('response__text', 'participant__name', 'evaluation__name')