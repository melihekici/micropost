from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)


class Micropost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    text = models.CharField(max_length=300)
    referenced = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="reference")
    timestamp = models.DateTimeField(auto_now=True)
