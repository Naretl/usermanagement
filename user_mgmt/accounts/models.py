
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    USER_TYPES = (
        ('community', 'Community Member'),
        ('staff', 'Staff'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='community')

    def __str__(self):
        return f"{self.user.username} ({self.user_type})"
