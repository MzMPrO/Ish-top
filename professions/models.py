from django.db import models


class ProfessionArea(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Profession Area"
        verbose_name_plural = "Profession Areas"

    def __str__(self):
        return f"{self.name}"


class Profession(models.Model):
    name = models.CharField(max_length=150, unique=True)
    profession_area = models.ForeignKey(
        ProfessionArea, related_name='profession_area', on_delete=models.PROTECT
    )


    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"

    def __str__(self):
        return f"{self.name}"
