from django.db import models
from GameList.models.developer import Developer
from GameList.models.genre import Genre
from GameList.models.official_web import Official_web
from GameList.models.platform import Platform
from GameList.models.publisher import Publisher

class Game(models.Model):
    title = models.CharField(max_length=200)    
    genre = models.ManyToManyField(Genre)
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    offical_web = models.OneToOneField(Official_web, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    platform = models.ManyToManyField(Platform)
    rating = models.DecimalField(max_digits=4,decimal_places=2, null=True, blank=True)
    date_published = models.DateField()
    description = models.TextField(max_length=1000)

    class meta:
        app_label = 'GameList'

    def __str__(self):
        return self.title