# Generated by Django 3.1.3 on 2020-11-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_candidateapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='status',
            field=models.IntegerField(choices=[(0, 'Любой'), (1, 'Москва'), (2, 'Калининград'), (3, 'Казань'), (4, 'Санкт-Петербург'), (5, 'Краснодар')], default=0, null=True),
        ),
    ]
