# Generated manually for Coderhouse final project
from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('subtitulo', models.CharField(max_length=180)),
                ('categoria', models.CharField(max_length=80)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='pages/')),
                ('fecha_publicacion', models.DateField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
                'ordering': ['-fecha_publicacion', '-creado'],
            },
        ),
    ]
