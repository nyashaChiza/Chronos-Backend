from rest_framework import serializers, viewsets
from evaluation.models import Tag, Attachment, Question, Response, Participant, Evaluation, Answer

class TagSerializer(serializers.ModelSerializer):
    number_of_evaluations = serializers.SerializerMethodField()
    
    def get_number_of_evaluations(self, obj):
        return obj.number_of_evaluations()
    class Meta:
        model = Tag
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class TagViewSet(viewsets.ModelViewSet):    
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class QuestionSerializer(serializers.ModelSerializer):
    number_of_answers = serializers.SerializerMethodField()
    least_selected_answer = serializers.SerializerMethodField()
    most_selected_answer = serializers.SerializerMethodField()

    def get_number_of_answers(self, obj):
        return obj.number_of_answers()

    def get_least_selected_answer(self, obj):
        if least_selected_answer := obj.least_selected_answer():
            return least_selected_answer.answer_text
        return None
    
    def get_most_selected_answer(self, obj):
        if most_selected_answer := obj.most_selected_answer():
            return most_selected_answer.answer_text
        return None

    class Meta:
        model = Question
        fields = '__all__'

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ResponseSerializer(serializers.ModelSerializer):
    response_time = serializers.SerializerMethodField()
    
    def get_response_time(self, obj):
        return response_time if (response_time := obj.response_time()) else None
    
    
    class Meta:
        model = Response
        fields = '__all__'

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    
class EvaluationSerializer(serializers.ModelSerializer):
    age_distribution = serializers.SerializerMethodField()
    gender_distribution = serializers.SerializerMethodField()

    def get_age_distribution(self, obj):
        # Calculate and return the age distribution
        # You can use the existing logic from the Evaluation model's age_distribution method
        return obj.age_distribution()

    def get_gender_distribution(self, obj):
        # Calculate and return the gender distribution
        # You can use the existing logic from the Evaluation model's gender_distribution method
        return obj.gender_distribution()
    class Meta:
        model = Evaluation
        fields = '__all__'

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer