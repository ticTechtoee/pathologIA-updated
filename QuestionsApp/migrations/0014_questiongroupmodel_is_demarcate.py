# Generated by Django 4.1.2 on 2023-05-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsApp', '0013_alter_mcqmodel_related_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiongroupmodel',
            name='Is_Demarcate',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
