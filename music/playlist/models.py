from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class PlayList(models.Model):
    title = models.CharField(max_length=30, default='No Title')
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    background = models.FileField(upload_to='playlist/')


class Song(models.Model):
    name_song = models.CharField(max_length=30, default='Music')
    mp3 = models.FileField(upload_to='audio/')
    background = models.FileField(upload_to='song/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_id = models.ForeignKey(PlayList, on_delete=models.CASCADE, default=1)
