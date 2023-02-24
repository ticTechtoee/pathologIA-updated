from django.db import migrations

def create_category(apps, schema_editor):
    Category = apps.get_model('QuestionsApp', 'QuestionTypesModel')
    Category.objects.create(Category='Multiple Choice Questions')
    Category.objects.create(Category='Demarcate Questions')


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_category),
    ]
