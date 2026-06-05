from django.contrib import admin
from .models import ArticuloFinanciero, ServicioFinanciero, ConsultaCliente

admin.site.register(ArticuloFinanciero)
admin.site.register(ServicioFinanciero)
admin.site.register(ConsultaCliente)
