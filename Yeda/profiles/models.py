from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='No bio ...')
    avatar = models.ImageField(default = 'no-image.png', upload_to = 'avatars')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username} created on {self.created.strftime('%d/%m/%Y')}"
    