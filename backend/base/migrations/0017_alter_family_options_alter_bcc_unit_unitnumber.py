# Generated by Django 4.1.3 on 2023-07-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_rename_socialaction_minstry_bcc_unit_social_action_minstry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ['unitnumber']},
        ),
        migrations.AlterField(
            model_name='bcc_unit',
            name='unitnumber',
            field=models.IntegerField(),
        ),
    ]
