from django.urls import include
from django.urls import path
from rest_framework import routers

from . import views

app_name = 'client'

router = routers.SimpleRouter()
router.register('', views.CourseViewSet, basename='courses')

urlpatterns = [
    path('courses/', include(router.urls)),
    path('teachbase/courses/', views.CoursesApiView.as_view()),
    path('teachbase/courses/<int:course_id>/', views.CourseApiView.as_view()),
    path('teachbase/users/create/', views.UserApiView.as_view()),
    path('teachbase/courses/<int:course_id>/course_sessions/',
         views.CourseSessionsApiView.as_view()),
    path('teachbase/course_sessions/<int:session_id>/register/',
         views.RegisterCourseSessionApiView.as_view()),

]
