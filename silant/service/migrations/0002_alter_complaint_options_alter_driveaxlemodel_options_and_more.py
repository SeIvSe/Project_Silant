# Generated by Django 4.2.1 on 2023-06-06 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'ordering': ['-date_rejection'], 'verbose_name': 'Рекламации', 'verbose_name_plural': 'Рекламации'},
        ),
        migrations.AlterModelOptions(
            name='driveaxlemodel',
            options={'verbose_name': 'Модель ведущего моста', 'verbose_name_plural': 'Модель ведущего моста'},
        ),
        migrations.AlterModelOptions(
            name='enginemodel',
            options={'verbose_name': 'Модель двигателя', 'verbose_name_plural': 'Модель двигателя'},
        ),
        migrations.AlterModelOptions(
            name='failurenode',
            options={'verbose_name': 'Характер отказа', 'verbose_name_plural': 'Характер отказа'},
        ),
        migrations.AlterModelOptions(
            name='machine',
            options={'ordering': ['-shipping_date'], 'verbose_name': 'Машина', 'verbose_name_plural': 'Машина'},
        ),
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-service_date'], 'verbose_name': 'Техническое обслуживание', 'verbose_name_plural': 'Техническое обслуживание'},
        ),
        migrations.AlterModelOptions(
            name='makeservicecompany',
            options={'verbose_name': 'Организация, проводившая ТО', 'verbose_name_plural': 'Организация, проводившая ТО'},
        ),
        migrations.AlterModelOptions(
            name='recoverymethod',
            options={'verbose_name': 'Способ восстановления', 'verbose_name_plural': 'Способ восстановления'},
        ),
        migrations.AlterModelOptions(
            name='servicecompany',
            options={'verbose_name': 'Сервисная компания', 'verbose_name_plural': 'Сервисная компания'},
        ),
        migrations.AlterModelOptions(
            name='servicetype',
            options={'verbose_name': 'Вид ТО', 'verbose_name_plural': 'Вид ТО'},
        ),
        migrations.AlterModelOptions(
            name='steeringbridgemodel',
            options={'verbose_name': 'Модель управляемого моста', 'verbose_name_plural': 'Модель управляемого моста'},
        ),
        migrations.AlterModelOptions(
            name='techniquemodel',
            options={'verbose_name': 'Модель техники', 'verbose_name_plural': 'Модель техники'},
        ),
        migrations.AlterModelOptions(
            name='transmissionmodel',
            options={'verbose_name': 'Модель трансмиссии', 'verbose_name_plural': 'Модель трансмиссии'},
        ),
    ]