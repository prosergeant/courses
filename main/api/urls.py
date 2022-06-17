from django.urls import path
from rest_framework import routers
from .views import QuizDataView, CourseDataViewSet, CustomUserViewSet, UserByToken, GetUserInfo, quiz_v2, TestAnswersViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = routers.SimpleRouter()
#router.register('quiz_v', QuizDataViewSet, basename="quiz")
router.register('course', CourseDataViewSet, basename='course')
router.register('users', CustomUserViewSet, basename='users')
router.register('test-answers', TestAnswersViewSet, basename='test-answers')

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('user/', UserByToken.as_view()),
    path('user-info/', GetUserInfo.as_view()),
    path('quiz/', QuizDataView.as_view()),
    path('quiz_v2/<int:pk>/', quiz_v2 ),
]
urlpatterns += router.urls