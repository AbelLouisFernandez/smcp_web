# Generated by Django 4.1.3 on 2023-07-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_result_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='time',
            field=models.CharField(max_length=15),
        ),
    ]
