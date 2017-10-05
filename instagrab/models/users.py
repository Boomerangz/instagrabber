from django.db import models


class InstaUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    parsed = models.BooleanField(default=False)
    followers = models.ManyToManyField("self", blank=True)

class Hashtag(models.Model):
    text = models.CharField(max_length=255, unique=True)

class Post(models.Model):
    user = models.ForeignKey(InstaUser)
    code = models.CharField(max_length=255, unique=True)
    likes = models.IntegerField()
    text = models.TextField(blank=False)
    hashtags = models.ManyToManyField(Hashtag, blank=True)


