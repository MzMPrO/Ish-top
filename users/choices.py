from django.db import models


class RoleChoices(models.TextChoices):
    ADMIN = ("admin", "Admin")
    EMPLOYEE = ("employee", "Employee")
    EMPLOYER = ("employer", "Employer")
