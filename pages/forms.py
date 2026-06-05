from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['titulo', 'subtitulo', 'categoria', 'contenido', 'imagen', 'fecha_publicacion']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }


class PageSearchForm(forms.Form):
    q = forms.CharField(
        max_length=100,
        required=False,
        label='Buscar',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por título o categoría'})
    )
