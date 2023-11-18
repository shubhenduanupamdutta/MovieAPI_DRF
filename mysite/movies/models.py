from django.db import models

# Create your models here.


class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=500, default="action")
    image = models.ImageField(upload_to="images/",
                              default="images/None/No-img.jpg")

    def __str__(self):
        return self.name
