from django.contrib import admin

from .models import Testing, TestingSolution

@admin.register(Testing)
class Testing(admin.ModelAdmin):
    list_display=('__str__', )

@admin.register(TestingSolution)
class TestingSolution(admin.ModelAdmin):
    list_display=('__str__', )