from django.db import models

class Developer(models.Model):
    nick_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Born', null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class meta:
        app_label = 'GameList'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
