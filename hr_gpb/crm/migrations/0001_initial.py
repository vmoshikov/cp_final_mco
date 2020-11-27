# Generated by Django 3.1.3 on 2020-11-27 16:29

import crm.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Навык', max_length=200, null=True)),
                ('type', models.IntegerField(choices=[(1, 'Hard skill'), (2, 'Soft skill')], default=1, null=True)),
                ('created', models.DateTimeField(default=crm.models.default_time)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Вакансия #', max_length=200, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Новая'), (1, 'В работе'), (100, 'Закрыта')], default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=crm.models.default_time)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vacancy_requaried_skills', models.ManyToManyField(blank=True, related_name='vacancy_requaried_skills', to='crm.Skills')),
                ('vacancy_skills', models.ManyToManyField(blank=True, related_name='vacancy_skills', to='crm.Skills')),
            ],
        ),
    ]