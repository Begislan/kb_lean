# Generated by Django 4.1.7 on 2023-03-15 15:38

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0004_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон номер'),
        ),
    ]