# Generated by Django 4.0.3 on 2022-04-06 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publications', '0002_alter_publication_volume_alter_publication_weight'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id_request', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('state', models.CharField(blank=True, default='Pendiente', max_length=30, null=True, verbose_name='Estado')),
                ('comments', models.CharField(blank=True, max_length=254, null=True, verbose_name='Comentarios')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activa')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.publication', verbose_name='Publicación')),
                ('recycler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Solicitante')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
                'ordering': ['-date'],
            },
        ),
    ]
