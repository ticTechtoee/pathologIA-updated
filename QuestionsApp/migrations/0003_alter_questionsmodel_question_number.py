# Generated by Django 4.1.2 on 2023-02-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsApp', '0002_create_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsmodel',
            name='Question_Number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
