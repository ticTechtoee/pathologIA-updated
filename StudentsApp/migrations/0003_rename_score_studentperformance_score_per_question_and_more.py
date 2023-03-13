# Generated by Django 4.1.2 on 2023-03-13 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentsApp', '0002_studentperformance_question_group_information_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentperformance',
            old_name='Score',
            new_name='Score_Per_Question',
        ),
        migrations.AlterField(
            model_name='studentperformance',
            name='Completed_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 13, 21, 22, 43, 688641, tzinfo=datetime.timezone.utc)),
        ),
    ]