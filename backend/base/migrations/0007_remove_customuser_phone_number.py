# Generated by Django 4.1.3 on 2023-08-24 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_phone_person_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
    ]