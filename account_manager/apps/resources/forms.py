from django import forms
from .models import Resource


class ResourceForm(forms.ModelForm):
    note = forms.CharField(required=False)

    class Meta:
        model = Resource
        fields = ('title', 'url', 'note')
        labels = {
            'title': 'Название ресурса',
            'url': 'Ссылка',
            'note': 'Примечание',
        }
