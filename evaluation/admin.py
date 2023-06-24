from django.contrib import admin
from .models import Evaluation, Tag, Attachment, Question, Response, Participant

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    list_filter = ('evaluation', )
    search_fields = ('name', 'evaluation__title')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'evaluation')
    list_filter = ('evaluation',)
    search_fields = ('text', 'evaluation__title')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('evaluation', 'participant', 'question', 'created')
    list_filter = ('evaluation', 'participant', 'question')
    search_fields = ('evaluation__title', 'participant__name', 'question__text')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created')
    search_fields = ('name', 'email')