from django.forms import ModelForm
from django.core.exceptions import ValidationError
from GameList.models.genre import Genre

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name','description']