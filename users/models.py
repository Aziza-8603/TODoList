from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}'s profile"

# class register(models.Model):
#     username = models.CharField(max_length=150)
#     email = models.EmailField()
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return self.username
    