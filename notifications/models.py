from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
