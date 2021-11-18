# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-16 18:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(bucket='tthomas-codalab-public'), upload_to='team_logo', verbose_name='Logo')),
                ('image_url_base', models.CharField(max_length=255)),
                ('allow_requests', models.BooleanField(default=True, verbose_name='Allow requests')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_invitation', models.BooleanField(default=False)),
                ('is_request', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Date (UTC)')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date (UTC)')),
                ('message', models.TextField(blank=True, null=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMembershipStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('codename', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeamStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('codename', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='teammembership',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.TeamMembershipStatus'),
        ),
        migrations.AddField(
            model_name='teammembership',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
        migrations.AddField(
            model_name='teammembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_memberships', to=settings.AUTH_USER_MODEL),
        ),
    ]
