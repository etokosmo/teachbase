from django.db import models


class Course(models.Model):
    name = models.CharField(
        help_text='Course name',
        max_length=100,
    )
    created_at = models.DateTimeField(
        help_text='Course created at',
    )
    updated_at = models.DateTimeField(
        help_text='Course updated at',
    )
    owner_id = models.IntegerField(
        help_text='Course creator id',
    )
    owner_name = models.TextField(
        help_text='Course creator name',
        max_length=100,
    )
    thumb_url = models.CharField(
        help_text='Course thumb cover url',
        max_length=200,
        blank=True,
    )
    cover_url = models.CharField(
        help_text='Course cover url',
        max_length=200,
        blank=True,
    )
    description = models.TextField(
        help_text='Course description',
    )
    last_activity = models.DateTimeField(
        help_text='Last author’s activity',
    )
    total_score = models.IntegerField(
        help_text='Max score listener can get',
    )
    total_tasks = models.IntegerField(
        help_text='Number of tasks in course',
    )
    unchangeable = models.BooleanField(
        help_text='Course changeable?',
        default=False,
    )
    include_weekly_report = models.BooleanField(
        help_text='Course statistics will be included in the weekly report',
        default=False,
    )
    content_type = models.PositiveSmallIntegerField(
        help_text='Course content type (course: 1, quiz: 2, literature: 3)',
    )
    is_netology = models.BooleanField(
        help_text='Course netology',
        default=False
    )
    bg_url = models.URLField(
        help_text='Background url',
        max_length=200,
        blank=True
    )
    video_url = models.URLField(
        help_text='Video url',
        max_length=200,
        blank=True,
    )
    demo = models.BooleanField(
        help_text='Course has demo',
        default=False,
    )
    custom_author_names = models.CharField(
        help_text='Custom course authors’ names (separated by comma). \
                    If present, takes precedence over authors collection.',
        max_length=200,
    )
    custom_contents_link = models.URLField(
        help_text='Redirection after registration/payment and the link for the “Back” button in the player',
        max_length=200,
        blank=True,
        null=True,
    )
    hide_viewer_navigation = models.BooleanField(
        help_text='Hide navigation in the player',
    )
    duration = models.IntegerField(
        help_text='Duration of the course (in sec.)',
        blank=True,
        null=True,
    )
    account_id = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
