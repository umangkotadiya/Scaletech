from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    role_name = models.CharField(max_length=255, unique=True)
    access_modules = models.JSONField() 
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.role_name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email
