from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)

    class meta:
        app_label = 'GameList'
        
    def __str__(self):
        return self.name