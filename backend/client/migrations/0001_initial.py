# Generated by Django 4.0.1 on 2023-04-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Course name', max_length=100)),
                ('created_at', models.DateTimeField(help_text='Course created at')),
                ('updated_at', models.DateTimeField(help_text='Course updated at')),
                ('owner_id', models.IntegerField(help_text='Course creator id')),
                ('owner_name', models.TextField(help_text='Course creator name', max_length=100)),
                ('thumb_url', models.CharField(blank=True, help_text='Course thumb cover url', max_length=200)),
                ('cover_url', models.CharField(blank=True, help_text='Course cover url', max_length=200)),
                ('description', models.TextField(help_text='Course description')),
                ('last_activity', models.DateTimeField(help_text='Last author’s activity')),
                ('total_score', models.IntegerField(help_text='Max score listener can get')),
                ('total_tasks', models.IntegerField(help_text='Number of tasks in course')),
                ('unchangeable', models.BooleanField(default=False, help_text='Course changeable?')),
                ('include_weekly_report', models.BooleanField(default=False, help_text='Course statistics will be included in the weekly report')),
                ('content_type', models.PositiveSmallIntegerField(help_text='Course content type (course: 1, quiz: 2, literature: 3)')),
                ('is_netology', models.BooleanField(default=False, help_text='Course netology')),
                ('bg_url', models.URLField(blank=True, help_text='Background url')),
                ('video_url', models.URLField(blank=True, help_text='Video url')),
                ('demo', models.BooleanField(default=False, help_text='Course has demo')),
                ('custom_author_names', models.CharField(help_text='Custom course authors’ names (separated by comma).                     If present, takes precedence over authors collection.', max_length=200)),
                ('custom_contents_link', models.URLField(blank=True, help_text='Redirection after registration/payment and the link for the “Back” button in the player', null=True)),
                ('hide_viewer_navigation', models.BooleanField(help_text='Hide navigation in the player')),
                ('duration', models.IntegerField(blank=True, help_text='Duration of the course (in sec.)', null=True)),
                ('account_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
