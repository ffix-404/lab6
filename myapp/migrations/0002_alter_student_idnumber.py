# Generated by Django 5.0.2 on 2024-03-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='idNumber',
            field=models.IntegerField(),
        ),
    ]
