# Generated by Django 4.1.2 on 2023-04-19 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentsApp', '0008_studentperformance_question_group_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentperformance',
            name='Question_Group_Information',
        ),
    ]