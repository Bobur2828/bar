# Generated by Django 5.1.2 on 2024-10-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='latitude',
            field=models.CharField(max_length=1000, verbose_name='Kenglik'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='longitude',
            field=models.CharField(max_length=1000, verbose_name='Uzunlik'),
        ),
    ]
