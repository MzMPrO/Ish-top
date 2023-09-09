from django.db import models


class RoleChoises(models.TextChoices):
    ADMIN = ("admin", 'Admin')
    EMPLOYEE = ("employee", 'Employee')
    EMPLOYER = ("employer", "Employer")