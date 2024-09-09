from django.db import models

# Create your models here.
class Movie(models.Model):
    Movie_Name=models.CharField(max_length=100);
    Poster=models.ImageField(upload_to='images');
    Date=models.CharField(max_length=100);

    def __str__(self):
        return self.Movie_Name
