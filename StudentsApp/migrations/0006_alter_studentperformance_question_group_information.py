# Generated by Django 4.1.2 on 2023-04-05 16:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsApp', '0010_alter_questionsmodel_question_text'),
        ('StudentsApp', '0005_alter_studentperformance_completed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentperformance',
            name='Question_Group_Information',
            field=models.ForeignKey(default=uuid.UUID('2fb3cf20-24d8-4e03-92d9-19e257fe89d8'), on_delete=django.db.models.deletion.DO_NOTHING, to='QuestionsApp.questiongroupmodel'),
        ),
    ]
