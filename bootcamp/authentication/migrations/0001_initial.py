# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 13:32
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=50, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('wallet', models.CharField(blank=True, max_length=50, null=True)),
                ('is_master', models.BooleanField(default=False)),
                ('weight', models.IntegerField(default=0)),
                ('tocken', models.UUIDField(default=uuid.uuid4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_profile',
            },
        ),
    ]
