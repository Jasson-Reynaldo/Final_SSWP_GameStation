from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    Founded_date= models.DateField()

    class meta:
        app_label = 'GameList'
        
    def __str__(self):
        return self.nam