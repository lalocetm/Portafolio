# Generated by Django 5.0.3 on 2024-03-11 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2024, 3, 10, 21, 7, 3, 400469)),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
    ]