# Generated by Django 5.1.2 on 2024-10-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0002_alter_contacts_latitude_alter_contacts_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='latitude',
            field=models.CharField(max_length=1000, verbose_name='Ish vaqti'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='longitude',
            field=models.TextField(verbose_name='Harita Iframini kiriting'),
        ),
    ]
