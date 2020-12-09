from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)

    class meta:
        app_label = 'GameList'
        
    def __str__(self):
        return self.name 