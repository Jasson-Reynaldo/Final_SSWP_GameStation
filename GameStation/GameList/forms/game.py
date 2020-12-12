from django.forms import ModelForm
from django.core.exceptions import ValidationError
from GameList.models.game import Game

class GameForm(ModelForm):
    class Meta:
        model = Game 
        fields = ['title', 'genre', 'developer', 'publisher','offical_web', 'price', 'platform', 'rating', 'date_published', 'description']
