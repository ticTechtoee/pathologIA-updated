# Generated by Django 4.1.2 on 2023-03-05 18:11

from django.db import migrations
def Create_ImageGroupModel(apps, schema_editor):
    ImageGroup = apps.get_model('ImagesApp', 'ImageGroupModel')
    ImageGroup.objects.create(Description = "Acupuntura")
    ImageGroup.objects.create(Description = "Alergia")
    ImageGroup.objects.create(Description = "Anestesiologia")
    ImageGroup.objects.create(Description = "Angiologia")
    ImageGroup.objects.create(Description = "Cardiologia")
    ImageGroup.objects.create(Description = "Coloproctologia")
    ImageGroup.objects.create(Description = "Dermatologia")
    ImageGroup.objects.create(Description = "Endocrinologia")
    ImageGroup.objects.create(Description = "Endoscopia")
    ImageGroup.objects.create(Description = "Gastroenterologia")
    ImageGroup.objects.create(Description = "Genetica")
    ImageGroup.objects.create(Description = "Geriatria")
    ImageGroup.objects.create(Description = "Ginecologia")
    ImageGroup.objects.create(Description = "Hematologia")
    ImageGroup.objects.create(Description = "Homeopatia")
    ImageGroup.objects.create(Description = "Infectologia")
    ImageGroup.objects.create(Description = "Mastologia")
    ImageGroup.objects.create(Description = "Nefrologia")
    ImageGroup.objects.create(Description = "Neurocirurgia")
    ImageGroup.objects.create(Description = "Neurologia")
    ImageGroup.objects.create(Description = "Nutrologia")
    ImageGroup.objects.create(Description = "Oftalmologia")
    ImageGroup.objects.create(Description = "Oncologia")
    ImageGroup.objects.create(Description = "Ortopedia")
    ImageGroup.objects.create(Description = "Otorrinolaringologia")
    ImageGroup.objects.create(Description = "Patologia")
    ImageGroup.objects.create(Description = "Pediatria")
    ImageGroup.objects.create(Description = "Pneumologia")
    ImageGroup.objects.create(Description = "Psiquiatria")
    ImageGroup.objects.create(Description = "Radiologia")
    ImageGroup.objects.create(Description = "Radioterapia")
    ImageGroup.objects.create(Description = "Reumatologia")
    ImageGroup.objects.create(Description = "Urologia")

class Migration(migrations.Migration):

    dependencies = [
        ('ImagesApp', '0003_Create_ImageTypes'),
    ]

    operations = [
        migrations.RunPython(Create_ImageGroupModel),
    ]
