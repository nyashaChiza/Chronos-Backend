from django.contrib import admin
from .models import Evaluation, Tag, Attachment, Question, Response, Participant, Answer, EvaluationInvite


@admin.register(EvaluationInvite)
class EvaluationInviteAdmin(admin.ModelAdmin):
    list_display = ('evaluation', 'participant','is_accepted' ,'is_valid',)
    list_filter = ('evaluation', 'participant','is_accepted' )
    search_fields = ('evaluation', 'participant','is_accepted' )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_text','weight' ,'is_selected',)
    list_filter = ('question', 'is_selected')
    search_fields = ('answer_text','question')


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_of_participants','number_of_responses','start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','number_of_evaluations')

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    list_filter = ('evaluation', )
    search_fields = ('name', 'evaluation__title')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'evaluation','number_of_answers','least_selected_answer', 'most_selected_answer')
    list_filter = ('evaluation',)
    search_fields = ('text', 'evaluation__title')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('evaluation', 'participant', 'question', 'answer','response_time','created')
    list_filter = ('evaluation', 'participant', 'question')
    search_fields = ('evaluation__title', 'participant__name', 'question__text')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','evaluation','created')
    search_fields = ('name', 'email')