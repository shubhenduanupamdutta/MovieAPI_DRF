from django.db import models

# Create your models here.


class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()

    def __str__(self):
        return self.name
