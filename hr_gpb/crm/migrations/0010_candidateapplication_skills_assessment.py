# Generated by Django 3.1.3 on 2020-11-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20201127_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateapplication',
            name='skills_assessment',
            field=models.JSONField(default=[]),
        ),
    ]
