from django.db import models

# Create your models here.

class Artist(models.Model):
    id=models.IntegerField()
    Name=models.TextField()


class Album(models.Model):
    id = models.IntegerField()
    Title = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Track(models.Model):
    id = models.IntegerField()
    Name = models.TextField()
    Composer=models.TextField()
    Miliseconds=models.TextField()
    Bytes=models.IntegerField()
    UnitPrice=models.FloatField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)