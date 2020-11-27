from django.db import models
from django.utils import timezone
from django.conf import settings
from model_utils import Choices

def default_time():
    return timezone.now()


class Skill(models.Model):
      TYPES = Choices(
            (1, "hard", "Hard skill"),
            (2, "soft", "Soft skill"),
        )
      title = models.CharField(max_length=200, null=True,
        blank=True, default="Навык")
      type = models.IntegerField(choices=TYPES, default=TYPES.hard, null=True)
      created = models.DateTimeField(default=default_time)

      def __str__(self):
        return f"{self.title} [{self.type}]"

class Vacancy(models.Model):
    STATUSES = Choices(
        (0, "new", "Новая"),
        (1, "execution", "В работе"),
        (100, "success", "Закрыта"),
    )
    title = models.CharField(max_length=200, null=True,
                            blank=True, default="Вакансия #")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES, default=STATUSES.new, null=True)
    vacancy_requaried_skills = models.ManyToManyField(
        Skill, blank=True, related_name="vacancy_requaried_skills"
    )
    vacancy_skills = models.ManyToManyField(
        Skill, blank=True, related_name="vacancy_skills"
    )
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=default_time)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
