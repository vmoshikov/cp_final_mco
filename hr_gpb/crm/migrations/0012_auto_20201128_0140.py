# Generated by Django 3.1.3 on 2020-11-27 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20201128_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateapplication',
            name='source',
            field=models.IntegerField(choices=[(0, 'Сайт'), (1, 'HeadHunter'), (2, 'SuperJob')], default=0),
        ),
        migrations.AlterField(
            model_name='candidateapplication',
            name='status',
            field=models.IntegerField(choices=[(0, 'Отказ'), (1, 'Новая'), (2, 'Тестирование'), (3, 'Собеседование'), (4, 'Служба безопасности'), (5, 'Оффер')], default=1),
        ),
    ]
