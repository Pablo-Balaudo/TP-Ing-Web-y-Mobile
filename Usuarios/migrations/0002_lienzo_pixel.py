# Generated by Django 3.1 on 2020-09-01 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lienzo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fechainicio', models.DateTimeField()),
                ('Fechafin', models.DateTimeField()),
                ('Guardado', models.BooleanField(default=False)),
                ('Bloqueado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='pixel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.PositiveIntegerField(default=0)),
                ('vidas', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
