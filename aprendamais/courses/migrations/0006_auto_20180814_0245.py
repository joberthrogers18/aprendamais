# Generated by Django 2.1 on 2018-08-14 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180814_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(verbose_name='Atalho'),
        ),
    ]
