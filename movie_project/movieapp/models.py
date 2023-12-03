from django.db import models


# Create your models here.
class Movie(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery', blank=True)

    def __str__(self):
        return '{}'.format(self.name)
