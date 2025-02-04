from django.db import models
from accounts.models import CustomUser
from django.conf import settings

class Content(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=30, unique=True)
    sentence = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class History(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.ForeignKey(Content, on_delete=models.CASCADE)
    typing_time = models.IntegerField()

    def __str__(self):
        return f"{ self.user } : { self.title }"
    
class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.ForeignKey(Content, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.user } : { self.title }"