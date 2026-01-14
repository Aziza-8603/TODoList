from django.db import models
from django.contrib.auth.models import User
# from users.models import Profile 

class Task(models.Model):
    # user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title