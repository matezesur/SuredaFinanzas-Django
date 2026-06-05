from django.db import models


class ArticuloFinanciero(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class ServicioFinanciero(models.Model):
    nombre = models.CharField(max_length=80)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class ConsultaCliente(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)
    mensaje = models.TextField()
    fecha_consulta = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} - {self.email}'
