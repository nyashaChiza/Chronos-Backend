from django.urls import include, path
from rest_framework import routers
from evaluation.views import EvaluationViewSet, TagViewSet, AttachmentViewSet, QuestionViewSet, ResponseViewSet, ParticipantViewSet, AnswerViewSet, EvaluationInviteViewSet

from evaluation.views import AcceptInviteAPIView


router = routers.DefaultRouter()
router.register(r'evaluations', EvaluationViewSet)
router.register(r'tags', TagViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'responses', ResponseViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'evaluation-invites', EvaluationInviteViewSet)


urlpatterns = [    
    path('', include(router.urls)),
    path('accept-invite/<str:invite_uuid>/', AcceptInviteAPIView.as_view(), name='accept-invite'),
]