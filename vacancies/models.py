from django.db import models

from professions.models import Profession
from resumes.models import Resume
from users.models import User


class Vacancy(models.Model):
    owner = models.ForeignKey(
        User, related_name='vacancy_owner', on_delete=models.PROTECT
    )
    profession = models.ForeignKey(
        Profession, related_name='vacancy_profession', on_delete=models.PROTECT
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    salary_from = models.BigIntegerField(null=True)
    salary_to = models.BigIntegerField(null=True)
    is_active = models.BooleanField(default=True)
    application = models.ManyToManyField(Resume, related_name='application', through='vacancies.Application')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancys"

    def __str__(self):
        return f"{self.title}"


class Application(models.Model):
    vacancy = models.ForeignKey(
        Vacancy, related_name='application_vacancy', on_delete=models.PROTECT
    )
    resume = models.ForeignKey(
        Resume, related_name='application_resume', on_delete=models.PROTECT
    )
    comment = models.TextField(null=True)

