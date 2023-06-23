# Generated by Django 4.1.2 on 2023-05-25 13:18

from django.db import migrations

def create_default_question_group(apps, schema_editor):
    Default_Question_Group = apps.get_model('QuestionsApp', 'QuestionGroupModel')
    
    Default_Question_Group.objects.create(Group_Number = 1, Name_Of_Group = 'Default', Subject_Description = 'Default Group, Do Not Remove it', Is_Demarcate = False, Online_Status = False)

class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsApp', '0014_questiongroupmodel_is_demarcate'),
    ]

    operations = [
        migrations.RunPython(create_default_question_group),
    ]