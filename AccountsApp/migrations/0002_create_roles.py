from django.db import migrations

def create_roles(apps, schema_editor):
    Role = apps.get_model('AccountsApp', 'RoleModel')
    Role.objects.create(Role_Type='teacher')
    Role.objects.create(Role_Type='student')
    Role.objects.create(Role_Type='guest')

class Migration(migrations.Migration):

    dependencies = [
        ('AccountsApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_roles),
    ]
