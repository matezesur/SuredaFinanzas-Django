from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Page(models.Model):
    titulo = models.CharField(max_length=120)
    subtitulo = models.CharField(max_length=180)
    categoria = models.CharField(max_length=80)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='pages/', blank=True, null=True)
    fecha_publicacion = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_publicacion', '-creado']
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'pk': self.pk})
