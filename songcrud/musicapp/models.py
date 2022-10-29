from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=250)
    date_released = models.DateField()
    likes = models.IntegerField()
    artist = models.ForeignKey(Artiste, on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)