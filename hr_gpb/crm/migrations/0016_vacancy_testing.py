# Generated by Django 3.1.3 on 2020-11-28 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_delete_testingsolution'),
        ('crm', '0015_auto_20201128_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='testing',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_test', to='tests.testing'),
        ),
    ]