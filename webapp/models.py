from django.db import models


class Genre(models.Model):
    category = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.category


class Movies(models.Model):
    popularity = models.FloatField(blank=True,null=True)
    director = models.CharField(max_length=150,blank=True,null=True)
    genre = models.ManyToManyField(Genre, blank=True)
    imdb_score = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

