from django.db import models
from django.utils import timezone
from django.conf import settings
from model_utils import Choices

from tests.models import Testing, TestingSolution 


def default_time():
    return timezone.now()

class Candidate(models.Model):
      fullname = models.CharField(max_length=200, null=True, blank=True)
      phone = models.CharField(max_length=24, null=True, blank=True)
      email = models.EmailField(max_length=254, null=True, blank=True)
      
      created = models.DateTimeField(default=default_time)
      updated = models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.fullname

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
        return f"{self.title}"

class Duty(models.Model):
    title = models.CharField(max_length=200, null=True,
        blank=True, default="Обязанность")
    created = models.DateTimeField(default=default_time)

    def __str__(self):
        return f"{self.title}"

class Сondition(models.Model):
    title = models.CharField(max_length=200, null=True,
        blank=True, default="Условие")

    created = models.DateTimeField(default=default_time)

    def __str__(self):
        return f"{self.title}"


class Vacancy(models.Model):
    STATUSES = Choices(
        (0, "new", "Новая"),
        (1, "execution", "В работе"),
        (100, "success", "Закрыта"),
    )
    CITIES = Choices(
        (0, "any", "Любой"),
        (1, "moscow", "Москва"),
        (2, "kaliningrad", "Калининград"),
        (3, "kazan", "Казань"),
        (4, "spb", "Санкт-Петербург"),
        (5, "krasnodar", "Краснодар"),
    )
    title = models.CharField(max_length=200, null=True,
                            blank=True, default="Вакансия #")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    
    recruter = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="vacancy_recruter", null=True, blank=True)
    status = models.IntegerField(choices=STATUSES, default=STATUSES.new, null=True)
    description = models.TextField(null=True, blank=True)
    duties = models.ManyToManyField(
        Duty, blank=True, related_name="vacancy_duties"
    )
    experience = models.IntegerField(null=True)
    
    key_skills = models.ManyToManyField(
        Skill, blank=True, related_name="vacancy_key_skills"
    )
    additional_skills = models.ManyToManyField(
        Skill, blank=True, related_name="vacancy_additional_skills"
    )
    conditions = models.ManyToManyField(
        Сondition, blank=True, related_name="vacancy_conditions"
    )
    city = models.IntegerField(choices=CITIES, default=CITIES.any, null=True)

    testing = models.ForeignKey(Testing, blank=True, null=True, default=None, related_name="vacancy_test", on_delete=models.CASCADE)

    code_reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="vacancy_code_reviewer", null=True, blank=True)

    created = models.DateTimeField(default=default_time)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class CandidateApplication(models.Model):
    SOURCES = Choices(
        (0, "website", "Сайт"),
        (1, "hh", "HeadHunter"),
        (2, "sj", "SuperJob"),
    )
    STATUS = Choices(
        (0, "decline", "Отказ"),
        (1, "new", "Новая"),
        (2, "interview", "Собеседование"),
        (3, "secure", "Служба безопасности"),
        (4, "offer", "Оффер"),
    )

    core_condidate = models.ForeignKey(
    Candidate, blank=True, related_name="condidate_applicatin", on_delete=models.CASCADE)
    core_vacancy = models.ForeignKey(
    Vacancy, blank=True, related_name="vacancy_applicatin", on_delete=models.CASCADE)

    testing_solution = models.ForeignKey(TestingSolution, blank=True, null=True, default=None, related_name="vacancy_test", on_delete=models.CASCADE)

    status = models.IntegerField(choices=STATUS, default=STATUS.new)
    source = models.IntegerField(choices=SOURCES, default=SOURCES.website)
    cv_file = models.FileField(null=True, blank=True)
    cv_recognition = models.TextField(null=True, blank=True)
    skills_assessment = models.JSONField(default={})
    key_skills_conformity = models.IntegerField(default=0)
    additional_skills_conformity = models.IntegerField(default=0)

    created = models.DateTimeField(default=default_time)

    def __str__(self):
        return f"{self.core_condidate} -> {self.core_vacancy} от {self.created}"