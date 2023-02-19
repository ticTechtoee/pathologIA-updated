from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class RoleModel(models.Model):
    Id_Role = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Role_Type = models.CharField(max_length=50)
    def __str__(self):
        return self.Role_Type

class CustomUserModel(AbstractUser):
    Id_User = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Full_Name = models.CharField(max_length=50, blank=True, null=True)
    Email = models.EmailField(unique=True, blank=False)
    Mobile_Number = models.CharField(max_length=15, blank=True, null=True)
    Role = models.ForeignKey(RoleModel, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.Email

    USERNAME_FIELD = 'Email'

