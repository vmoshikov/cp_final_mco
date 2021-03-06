# Generated by Django 3.1.3 on 2020-11-28 09:04

from django.db import migrations, models
import django.db.models.deletion
import tests.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0015_auto_20201128_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Задача #', max_length=200, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(default=tests.models.default_time)),
            ],
        ),
        migrations.CreateModel(
            name='TestingSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('core_condidate', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='condidate_application_solution', to='crm.candidate')),
                ('core_vacancy', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_solution', to='crm.candidateapplication')),
            ],
        ),
    ]
