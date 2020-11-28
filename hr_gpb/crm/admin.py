from django.contrib import admin

from .models import Candidate, Vacancy, Skill, Duty, Сondition, CandidateApplication


@admin.register(Vacancy)
class Vacancy(admin.ModelAdmin):
    list_display=('title', 'owner', 'deadline', )

@admin.register(Candidate)
class Candidate(admin.ModelAdmin):
    list_display=('fullname', 'created', )


@admin.register(Skill)
class Skill(admin.ModelAdmin):
    list_display=('title', 'type' )

@admin.register(Duty)
class Duty(admin.ModelAdmin):
    list_display=('title', )

@admin.register(Сondition)
class Сondition(admin.ModelAdmin):
    list_display=('title',)

@admin.register(CandidateApplication)
class CandidateApplication(admin.ModelAdmin):
    list_display=('__str__', )