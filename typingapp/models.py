from django.db import models
from accounts.models import CustomUser

class Content(models.Model):
    created_by = models.ForeignKey(CustomUser,)
    title = models.CharField(max_length=30, unique=True)
    sentence = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class History(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    typing_time = models.IntegerField()

    def __str__(self):
        return f"{ self.user } : { self.content }"
    
class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.user } : { self.content }"