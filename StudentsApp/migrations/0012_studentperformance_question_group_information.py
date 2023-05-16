# Generated by Django 4.1.2 on 2023-05-16 13:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsApp', '0014_questiongroupmodel_is_demarcate'),
        ('StudentsApp', '0011_remove_studentperformance_question_group_information_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentperformance',
            name='Question_Group_Information',
            field=models.ForeignKey(default=uuid.UUID('6a48c8c0-00f6-43d2-ab32-32f99813e54f'), on_delete=django.db.models.deletion.DO_NOTHING, to='QuestionsApp.questiongroupmodel'),
        ),
    ]
