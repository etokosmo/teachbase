from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            'owner_id',
            'owner_name',
            'thumb_url',
            'cover_url',
            'description',
            'last_activity',
            'total_score',
            'total_tasks',
            'unchangeable',
            'include_weekly_report',
            'content_type',
            'is_netology',
            'bg_url',
            'video_url',
            'demo',
            'custom_author_names',
            'custom_contents_link',
            'hide_viewer_navigation',
            'duration',
        )

    def create(self, validated_data):
        teachbase_id = validated_data.pop('id', None)
        course, _ = Course.objects.get_or_create(
            id=teachbase_id,
            defaults={**validated_data},
        )
        return course
