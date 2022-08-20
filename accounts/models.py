from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return "%s with %s years old and staff is %s" % (self.username, self.age, self.is_staff)
