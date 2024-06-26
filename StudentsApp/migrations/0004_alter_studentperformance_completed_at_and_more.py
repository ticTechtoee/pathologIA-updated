# Generated by Django 4.1.2 on 2023-03-18 20:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsApp', '0010_alter_questionsmodel_question_text'),
        ('StudentsApp', '0003_rename_score_studentperformance_score_per_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentperformance',
            name='Completed_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 20, 11, 43, 223403, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studentperformance',
            name='Question_Group_Information',
            field=models.ForeignKey(default=uuid.UUID('0afdb817-4ea4-4cf0-a2e7-d976dc60545a'), on_delete=django.db.models.deletion.DO_NOTHING, to='QuestionsApp.questiongroupmodel'),
        ),
    ]
