from django import forms
from .models import ArticuloFinanciero, ServicioFinanciero, ConsultaCliente


class ArticuloFinancieroForm(forms.ModelForm):
    class Meta:
        model = ArticuloFinanciero
        fields = ['titulo', 'categoria', 'contenido']


class ServicioFinancieroForm(forms.ModelForm):
    class Meta:
        model = ServicioFinanciero
        fields = ['nombre', 'tipo', 'descripcion']


class ConsultaClienteForm(forms.ModelForm):
    class Meta:
        model = ConsultaCliente
        fields = ['nombre', 'email', 'telefono', 'mensaje']


class BusquedaArticuloForm(forms.Form):
    busqueda = forms.CharField(max_length=100, required=False, label='Buscar artículo')
