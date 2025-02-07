from django.db import models
from accounts.models import CustomUser
from contentapp.models import Content
    
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