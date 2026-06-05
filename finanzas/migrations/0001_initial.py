# Generated manually for the Coderhouse delivery

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticuloFinanciero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=50)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConsultaCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=30)),
                ('mensaje', models.TextField()),
                ('fecha_consulta', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServicioFinanciero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('tipo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
