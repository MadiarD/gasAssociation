from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_message')
    created_at = models.DateTimeField(auto_now_add=True)
    answers = models.ManyToManyField('self', related_name='answer', symmetrical= False, blank=True)
    public = models.BooleanField(default=False)
    def __str__(self):
        return self.message
