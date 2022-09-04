from django.db import models


class UserInfo(models.Model):
    age = models.IntegerField()
    size = models.IntegerField()


class AccessRecord(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
