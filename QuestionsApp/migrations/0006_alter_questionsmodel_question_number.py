# Generated by Django 4.1.2 on 2023-03-07 20:10

import QuestionsApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsApp', '0005_questiongroupmodel_group_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsmodel',
            name='Question_Number',
            field=models.IntegerField(default=QuestionsApp.models.QuestionsModel.number, unique=True),
        ),
    ]