# Generated by Django 5.1.3 on 2024-12-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]