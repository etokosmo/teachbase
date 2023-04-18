import os

import requests
from django.conf import settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Course
from .serializers import CourseSerializer
from .services import get_token


class CourseViewSet(ModelViewSet):
    """Get all Courses/one Course detail information from db"""

    serializer_class = CourseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Course.objects.all()
        if course_id := self.kwargs.get(self.lookup_field):
            return queryset.filter(id=course_id)
        return queryset


class CoursesApiView(APIView):
    """Get List of Courses from Teachbase API"""

    def get(self, request):
        courses_uri = 'endpoint/v1/courses/'
        get_courses_url = os.path.join(
            settings.TEACHBASE_API,
            courses_uri,
        )
        headers = {
            'Authorization': f'Bearer {get_token()}'
        }

        response = requests.get(
            get_courses_url,
            headers=headers,
            params=request.query_params,
        )

        return Response(response.json())


class CourseApiView(APIView):
    """Get Course by id from Teachbase API"""

    def get(self, request, course_id: int):
        """Get Course by id from Teachbase API"""
        courses_uri = f'endpoint/v1/courses/{course_id}'
        get_courses_url = os.path.join(
            settings.TEACHBASE_API,
            courses_uri,
        )
        headers = {
            'Authorization': f'Bearer {get_token()}'
        }
        response = requests.get(get_courses_url, headers=headers)

        return Response(response.json())

    def post(self, request, course_id: int):
        """Save in db Course by id from Teachbase API"""
        course = self.get(request, course_id).data

        serializer = CourseSerializer(data=course)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data)


class UserApiView(APIView):
    """Create User in Teachbase"""

    def post(self, request):
        create_user_uri = 'endpoint/v1/users/create/'
        create_user_url = os.path.join(
            settings.TEACHBASE_API,
            create_user_uri,
        )
        headers = {
            'Authorization': f'Bearer {get_token()}'
        }

        response = requests.post(
            create_user_url,
            headers=headers,
            json=request.data,
        )

        return Response(response.json())


class CourseSessionsApiView(APIView):
    """Get all sessions of Course in Teachbase"""

    def get(self, request: Request, course_id: int) -> Response:
        sessions_uri = f'endpoint/v1/courses/{course_id}/course_sessions/'
        sessions_url = os.path.join(
            settings.TEACHBASE_API,
            sessions_uri,
        )
        headers = {
            'Authorization': f'Bearer {get_token()}'
        }

        response = requests.get(
            sessions_url,
            headers=headers,
            params=request.query_params,
        )

        return Response(response.json())


class RegisterCourseSessionApiView(APIView):
    """Register user at Course' Session in Teachbase"""

    def post(self, request, session_id: int):
        register_uri = f'endpoint/v1/course_sessions/{session_id}/register/'
        register_url = os.path.join(
            settings.TEACHBASE_API,
            register_uri,
        )
        headers = {
            'Authorization': f'Bearer {get_token()}'
        }

        response = requests.post(
            register_url,
            headers=headers,
            json=request.data,
        )

        return Response(response.json())
