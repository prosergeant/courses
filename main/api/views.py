from rest_framework import viewsets

from .serializers import QuizDataSerializer, CourseDataSerializer, CustomUserSerializer, QuizSerializer, TestAnswersSerializer

from ..models import QuizData, Course, CustomUser, TestAnswers

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

"""
class QuizDataViewSet(viewsets.ModelViewSet):
    queryset = QuizData.objects.all()
    serializer_class = QuizSerializer
"""

@api_view(['GET'])
def quiz_v2(request, pk):
    instance = QuizData.objects.filter(course_id=pk) #.get(pk=pk)
    serializer = QuizSerializer(instance, many=True)
    return Response({ 'results': serializer.data})

class QuizDataView(APIView):
    
    def get(self, request, format=None):
        quiz = QuizData.objects.all()

        """
        data = {
            "question": quiz.question,
            "correct_answers": quiz.option_one,
            "incorrect_answers": [
                quiz.option_two,
                quiz.option_three,
                quiz.option_four
            ],
            "lesson_id": quiz.course_id
        }
        """

        queryset = quiz.values()


        return Response({ 'results': list(queryset) })


class CourseDataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseDataSerializer


class CustomUserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserByToken(APIView):
    def post(self, request, format=None):
        data = {
            "id": str(request.user.id),
            "email": str(request.user.email)
        }
        return Response(data, status=status.HTTP_201_CREATED)


class GetUserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        lvl = request.user.lvl
        exp = request.user.exp
        points = request.user.points
        email = request.user.email

        if (exp/10) > lvl:
            lvl = lvl + 1
            request.user.lvl = lvl
            request.user.save()

        data = {
            "lvl": lvl,
            "exp": exp,
            "points": points,
            "email": email,
            "id": request.user.id
        }

        return Response(data)


class TestAnswersViewSet(viewsets.ModelViewSet):

    queryset = TestAnswers.objects.all()
    serializer_class = TestAnswersSerializer