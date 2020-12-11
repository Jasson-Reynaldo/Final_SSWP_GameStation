from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    founder_name= models.CharField(max_length=500)
    founded_date= models.DateField()
    HQ_city = models.CharField(max_length=200)
    HQ_country= models.CharField(max_length=200)
    class meta:
        app_label = 'GameList'
        
    def __str__(self):
        return self.name