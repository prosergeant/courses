from django.urls import path
from . import views
from .views import CourseDetailView, ClassesDetailView, KlassDetailView, DirDetailView, CabinetView, BuyLessonView
from .views import SubjectDetailView, CabinetMyLessView, CSchoolRating, CSchoolRatingDetail
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.ab, name='about'),
    path('course', views.course, name='course'),
    # path(r'^lessons/<int:pk>', views.LessonDetail.as_view(), name='lessons-detail'),
    url(r'^lessons/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    # path('accounts/profile', views.cabinet, name='cabinet'),
    url('accounts/profile', CabinetView.as_view(), name='cabinet'),
    path('classes', views.classes, name="classes"),
    url(r'^classes/(?P<klass_id>\d+)/$', KlassDetailView.as_view(), name="direction_set"),
    url(r'^classes/(?P<klass_id>\d+)/(?P<dir_id>\w+)/$', DirDetailView.as_view(), name="direction_pick"),
    url(r'^classes/(?P<klass_id>\d+)/(?P<dir_id>\w+)/(?P<sub_id>\w+)/$', SubjectDetailView.as_view(), name="subject_set"),
    url(r'^classes/(?P<klass_id>\d+)/(?P<dir_id>\w+)/(?P<sub_id>\w+)/(?P<classes_id>\d+)/$', ClassesDetailView.as_view(), name="classes_detail"),
    url('registration/', views.RegisterFunc, name="registration"),
    url(r'^prebuy/(?P<lesson_id>\d+)/$', BuyLessonView.as_view(), name="pre_buy"),
    url(r'^buy/(?P<course_id>\d+)/$', views.Buy, name="buy"),
    url('my-lessons', CabinetMyLessView.as_view(), name='cabinet-myless'),
    url(r'^rating/$', CSchoolRating.as_view(), name='school-rating'),
    url(r'^rating/detail/$', CSchoolRatingDetail.as_view(), name='rating-detail')
]
