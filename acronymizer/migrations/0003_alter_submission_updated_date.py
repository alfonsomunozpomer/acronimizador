# Generated by Django 5.0.6 on 2024-06-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acronymizer', '0002_rename_acronymtoken_preposition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
