# Generated by Django 4.1.2 on 2023-05-16 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DemarcateApp', '0003_demarcatequestionsmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demarcatequestionsmodel',
            name='Image_For_Question',
        ),
        migrations.AlterField(
            model_name='demarcatequestion',
            name='Related_Question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DemarcateApp.demarcatequestionsmodel', verbose_name='Related Question'),
        ),
    ]
