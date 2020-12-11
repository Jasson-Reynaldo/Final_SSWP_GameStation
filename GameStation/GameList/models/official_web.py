from django.db import models

class Official_web(models.Model):
    name = models.CharField(max_length=200)

    class meta:
        app_label = 'GameList'

    def __str__(self):
        return self.name 