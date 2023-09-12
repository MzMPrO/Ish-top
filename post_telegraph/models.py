from django.db import models


class PostTelegraph(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField()
