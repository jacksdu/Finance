# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='port',
        ),
        migrations.AddField(
            model_name='host',
            name='password',
            field=models.CharField(default='mima', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='username',
            field=models.CharField(default='zhanghao', max_length=30),
            preserve_default=False,
        ),
    ]