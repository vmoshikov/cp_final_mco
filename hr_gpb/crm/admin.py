from django.contrib import admin

from .models import Vacancy, Skill, Duty, Сondition


@admin.register(Vacancy)
class Vacancy(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display=('title', 'owner', 'deadline', )

@admin.register(Skill)
class Skill(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display=('title', 'type' )

@admin.register(Duty)
class Duty(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display=('title', )

@admin.register(Сondition)
class Сondition(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display=('title',)