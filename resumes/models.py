from django.db import models

from professions.models import Profession
from users.models import User


class Resume(models.Model):
    owner = models.OneToOneField(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="resume/", null=True)
    profession = models.ForeignKey(
        Profession, related_name="resume_profession", on_delete=models.PROTECT
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return f"{self.title}"

