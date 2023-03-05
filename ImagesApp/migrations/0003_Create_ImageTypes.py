# Generated by Django 4.1.2 on 2023-03-05 18:08

from django.db import migrations
def Create_ImageTypes(apps, schema_editor):
    ImageType = apps.get_model('ImagesApp', 'ImageTypeModel')
    ImageType.objects.create(Description = "Angiografia")
    ImageType.objects.create(Description = "Densitometria ossea")
    ImageType.objects.create(Description = "Mamografia")
    ImageType.objects.create(Description = "Medicina nuclear")
    ImageType.objects.create(Description = "Raio-x")
    ImageType.objects.create(Description = "Ressonancia magnetica")
    ImageType.objects.create(Description = "Tomografia computadorizada")
    ImageType.objects.create(Description = "Ultrassonografia")

class Migration(migrations.Migration):

    dependencies = [
        ('ImagesApp', '0002_remove_imagemodel_path_to_folder'),
    ]

    operations = [
        migrations.RunPython(Create_ImageTypes),
    ]
