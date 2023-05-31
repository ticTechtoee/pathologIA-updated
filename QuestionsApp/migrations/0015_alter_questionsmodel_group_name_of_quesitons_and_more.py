# Generated by Django 4.1.2 on 2023-05-30 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VideosApp', '0001_initial'),
        ('QuestionsApp', '0014_questiongroupmodel_is_demarcate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsmodel',
            name='Group_Name_Of_Quesitons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='QuestionsApp.questiongroupmodel', verbose_name='Group Name of Subject'),
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='Type_Of_Question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='QuestionsApp.questiontypesmodel', verbose_name='Type of Question'),
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='Video_For_Question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VideosApp.videomodel', verbose_name='Link Video'),
        ),
    ]
