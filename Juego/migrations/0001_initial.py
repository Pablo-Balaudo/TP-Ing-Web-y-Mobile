# Generated by Django 3.1 on 2020-09-27 02:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Red', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(256)])),
                ('Green', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(256)])),
                ('Blue', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(256)])),
                ('Alpha', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(256)])),
            ],
            options={
                'unique_together': {('Nombre',)},
            },
        ),
        migrations.CreateModel(
            name='Lienzo',
            fields=[
                ('idLienzo', models.AutoField(primary_key=True, serialize=False)),
                ('fechainicio', models.DateTimeField(auto_now_add=True)),
                ('fechafin', models.DateTimeField(default=None, null=True)),
                ('tamano_max_X', models.IntegerField(default=51)),
                ('tamano_max_Y', models.IntegerField(default=51)),
                ('guardado', models.BooleanField(default=False)),
                ('principal', models.BooleanField(default=False)),
                ('bloqueado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pixel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenadaX', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(51)])),
                ('coordenadaY', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(51)])),
                ('Red', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(256)])),
                ('Green', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(256)])),
                ('Blue', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(256)])),
                ('Alpha', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(256)])),
                ('vidas', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)])),
                ('dueño', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('lienzo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Juego.lienzo')),
            ],
            options={
                'unique_together': {('coordenadaX', 'coordenadaY', 'lienzo')},
            },
        ),
        migrations.CreateModel(
            name='Jugada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juego.color')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pixel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juego.pixel')),
            ],
        ),
    ]
