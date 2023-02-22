# Generated by Django 4.1.2 on 2023-02-22 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ImagesApp', '0001_initial'),
        ('VideosApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionGroupModel',
            fields=[
                ('Id_QuestionGroup', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Name_Of_Group', models.CharField(blank=True, max_length=150, null=True)),
                ('Subject_Description', models.CharField(blank=True, max_length=250, null=True)),
                ('Date_Of_Creation', models.DateTimeField(blank=True, null=True)),
                ('Online_Status', models.IntegerField(blank=True, null=True)),
                ('Creators_Information', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTypesModel',
            fields=[
                ('Id_Type_Question', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Category', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsModel',
            fields=[
                ('Id_Question', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Question_Number', models.IntegerField(editable=False, unique=True)),
                ('Question_Text', models.CharField(blank=True, max_length=1000, null=True)),
                ('Question_Marks', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Correct_Answer', models.CharField(blank=True, default='A', max_length=1, null=True)),
                ('Group_Name_Of_Quesitons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='QuestionsApp.questiongroupmodel', verbose_name='Group Name of Subject')),
                ('Image_For_Quesiton', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ImagesApp.imagemodel', verbose_name='Link Image')),
                ('Type_Of_Question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='QuestionsApp.questiontypesmodel', verbose_name='Type of Question')),
                ('Video_For_Quesiton', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='VideosApp.videomodel', verbose_name='Link Video')),
            ],
        ),
        migrations.CreateModel(
            name='MCQModel',
            fields=[
                ('Id_MCQs', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Option', models.CharField(blank=True, max_length=1, null=True)),
                ('Option_Text', models.CharField(blank=True, max_length=1000, null=True)),
                ('Related_Question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='QuestionsApp.questionsmodel', verbose_name='Related Question')),
            ],
        ),
    ]
