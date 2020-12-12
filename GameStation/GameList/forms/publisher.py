from django.forms import ModelForm
from django.core.exceptions import ValidationError
from GameList.models.publisher import Publisher

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name','founder_name','founded_date','HQ_city','HQ_country']