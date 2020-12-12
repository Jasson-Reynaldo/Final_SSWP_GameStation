from django.forms import ModelForm
from django.core.exceptions import ValidationError
from GameList.models.platform import Platform

class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields=['name', 'creator'] 