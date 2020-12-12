from django.forms import ModelForm
from django.core.exceptions import ValidationError
from GameList.models.developer import Developer


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['nick_name', 'first_name', 'last_name', 'date_of_birth', 'date_of_death']