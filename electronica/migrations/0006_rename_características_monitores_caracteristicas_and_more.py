# Generated by Django 4.0.4 on 2022-06-05 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronica', '0005_alter_monitores_características'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitores',
            old_name='características',
            new_name='caracteristicas',
        ),
        migrations.RenameField(
            model_name='perifericos',
            old_name='características',
            new_name='caracteristicas',
        ),
    ]
