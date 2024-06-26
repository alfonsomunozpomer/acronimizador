# Generated by Django 5.0.6 on 2024-06-03 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=25)),
                ('sent_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1)),
                ('updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AcronymToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=25)),
                ('preposition', models.CharField(choices=[('desde', 'desde'), ('hasta', 'hasta'), ('entre', 'entre'), ('mediante', 'mediante'), ('con', 'con'), ('cabe', 'cabe'), ('tras', 'tras'), ('por', 'por'), ('a', 'a'), ('bajo', 'bajo'), ('según', 'según'), ('en', 'en'), ('hacia', 'hacia'), ('ante', 'ante'), ('contra', 'contra'), ('sobre', 'sobre'), ('de', 'de'), ('para', 'para'), ('so', 'so'), ('sin', 'sin'), ('durante', 'durante')], max_length=8, null=True)),
                ('order', models.IntegerField()),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acronymizer.submission')),
            ],
        ),
    ]
