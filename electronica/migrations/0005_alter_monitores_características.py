# Generated by Django 4.0.4 on 2022-06-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronica', '0004_monitores_características'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitores',
            name='características',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
