from django.db import models

from datetime import datetime

class UserIP(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=30)

    def __str__(self):
        return "<User IP: %r>" % self.ip

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=datetime.utcnow)
    user = models.ForeignKey(UserIP, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "<City %r>" % self.name

class Support(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(default=datetime.utcnow)
    user = models.ForeignKey(UserIP, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "<Support %r>" % self.id