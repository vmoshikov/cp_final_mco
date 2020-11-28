from django.db import models
from django.utils import timezone
from django.conf import settings
from model_utils import Choices


def default_time():
    return timezone.now()

class Testing(models.Model):
    TYPES = Choices(
        (0, "code", "Код"),
        (1, "text", "Текст"),
        (2, "creative", "Творческая"),
    )
    title = models.CharField(max_length=200, null=True,
                            blank=True, default="Задача #")
    type = models.IntegerField(choices=TYPES, default=TYPES.code)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    created = models.DateTimeField(default=default_time)

    def __str__(self):
        return f"{self.title}"

class TestingSolution(models.Model):
    STATUSES = Choices(
        (0, "decline", "Отклонено"),
        (1, "new", "Новое"),
        (2, "success", "Подтверждено"),
    )
    description =  models.TextField(null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    type = models.IntegerField(choices=STATUSES, default=STATUSES.new)

    def __str__(self):
        return f"Решение {self.id} на вакансию {self.vacancy_test}"