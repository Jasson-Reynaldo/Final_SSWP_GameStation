from django.forms import ModelForm
from django.core.exceptions import ValidationError
from GameList.models.official_web import Official_web


class Official_webForm(ModelForm):
    class Meta:
        model = Official_web
        fields = ['name']