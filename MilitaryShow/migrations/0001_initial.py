# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2021-01-29 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('userName', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
            ],
        ),
    ]
