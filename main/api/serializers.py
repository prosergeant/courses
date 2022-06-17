from rest_framework import serializers
from ..models import QuizData, Course, CustomUser, TestAnswers

class QuizDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizData
        fields = '__all__'


class CourseDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


"""
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['account_url', 'account_name', 'users', 'created']
        extra_kwargs = {
            'url': {'view_name': 'accounts', 'lookup_field': 'account_name'},
            'users': {'lookup_field': 'username'}
        }
"""

class QuizSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'course_id': instance.course_id,
            'question': instance.question,
            'correct_answer': instance.option_one,
            'incorrect_answers': [
                instance.option_two,
                instance.option_three,
                instance.option_four
            ]
        }


class TestAnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestAnswers
        fields = '__all__'