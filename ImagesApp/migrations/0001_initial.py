# Generated by Django 4.1.2 on 2023-02-22 12:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGroupModel',
            fields=[
                ('Id_Group', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Description', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('Id_Image', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Path_To_Folder', models.CharField(blank=True, max_length=250, null=True)),
                ('Upload_Image', models.ImageField(blank=True, null=True, upload_to='question_images/')),
                ('Image_Group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ImagesApp.imagegroupmodel', verbose_name='Group To Which This Image Belongs To')),
            ],
        ),
        migrations.CreateModel(
            name='ImageTypeModel',
            fields=[
                ('Id_Type_Image', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Description', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImagesQuestionsModel',
            fields=[
                ('Id_Images_Questions', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Id_Image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ImagesApp.imagemodel')),
            ],
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='Type_Of_Image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ImagesApp.imagetypemodel'),
        ),
    ]
