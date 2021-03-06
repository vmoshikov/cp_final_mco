# Generated by Django 3.1.3 on 2020-11-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20201127_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='vacancy_requaried_skills',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='vacancy_skills',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='additional_skills',
            field=models.ManyToManyField(blank=True, related_name='vacancy_additional_skills', to='crm.Skill'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='conditions',
            field=models.ManyToManyField(blank=True, related_name='vacancy_conditions', to='crm.Duty'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='duties',
            field=models.ManyToManyField(blank=True, related_name='vacancy_duties', to='crm.Duty'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='key_skills',
            field=models.ManyToManyField(blank=True, related_name='vacancy_key_skills', to='crm.Skill'),
        ),
    ]
