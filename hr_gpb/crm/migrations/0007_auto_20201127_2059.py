# Generated by Django 3.1.3 on 2020-11-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='conditions',
            field=models.ManyToManyField(blank=True, related_name='vacancy_conditions', to='crm.Сondition'),
        ),
    ]