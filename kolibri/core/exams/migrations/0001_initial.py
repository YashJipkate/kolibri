# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-16 22:34
from __future__ import unicode_literals

import django.db.models.deletion
import jsonfield.fields
import morango.utils.uuids
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kolibriauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('_morango_dirty_bit', models.BooleanField(default=True, editable=False)),
                ('_morango_source_id', models.CharField(editable=False, max_length=96)),
                ('_morango_partition', models.CharField(editable=False, max_length=128)),
                ('title', models.CharField(max_length=200)),
                ('channel_id', models.CharField(max_length=32, blank=True)),
                ('question_count', models.IntegerField()),
                ('question_sources', jsonfield.fields.JSONField(blank=True, default=[])),
                ('seed', models.IntegerField(default=1)),
                ('active', models.BooleanField(default=False)),
                ('archive', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='kolibriauth.Collection')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='kolibriauth.FacilityUser')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExamAssignment',
            fields=[
                ('id', morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('_morango_dirty_bit', models.BooleanField(default=True, editable=False)),
                ('_morango_source_id', models.CharField(editable=False, max_length=96)),
                ('_morango_partition', models.CharField(editable=False, max_length=128)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_exams', to='kolibriauth.FacilityUser')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_exams', to='kolibriauth.Collection')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='exams.Exam')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
