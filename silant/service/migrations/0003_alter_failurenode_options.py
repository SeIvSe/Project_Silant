# Generated by Django 4.2.1 on 2023-06-07 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_complaint_options_alter_driveaxlemodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='failurenode',
            options={'verbose_name': 'Описание отказа', 'verbose_name_plural': 'Описание отказа'},
        ),
    ]
