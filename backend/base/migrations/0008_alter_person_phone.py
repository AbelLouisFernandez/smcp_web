# Generated by Django 4.1.3 on 2023-07-15 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_person_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
