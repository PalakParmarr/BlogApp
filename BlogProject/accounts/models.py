from django.db import models
from django.contrib.auth.models import AbstractUser
Role = (
    ("visitor", "visittor"),
    ("author", "author"),
)

class TimeStamp(models.Model):
    """create dates and update date fields in this model"""
    created_at = models.DateField(auto_now_add=True, null=True)
    update_at = models.DateField(auto_now_add=True, null=True)


class User(AbstractUser):
    """Abstract User table"""
    first_name = models.CharField(max_length=122, null=True, blank=True)
    last_name = models.CharField(max_length=122, null=True, blank=True)
    role = models.CharField(max_length=50, choices=Role, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)


