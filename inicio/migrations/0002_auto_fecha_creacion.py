# Generated by Django 5.1.5 on 2025-02-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
    ]
