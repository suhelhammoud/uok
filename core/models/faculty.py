# from django.contrib.auth.models import AbstractUser
# from django.db.models import CharField
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _

from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    def __repr__(self):
        return self.caption
