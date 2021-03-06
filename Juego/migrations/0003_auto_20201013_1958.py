# Generated by Django 3.1 on 2020-10-13 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Usuarios', '0003_denuncia_denunciausuario'),
        ('Juego', '0002_auto_20201002_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='DenunciaJugadasHeader',
            fields=[
                ('denuncia_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      to='Usuarios.denuncia')),
                ('idDenunciaJugada', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('Usuarios.denuncia',),
        ),
        migrations.AlterModelOptions(
            name='jugada',
            options={'ordering': ['-fecha_creacion']},
        ),
        migrations.CreateModel(
            name='DenunciaJugadasDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juego.denunciajugadasheader')),
                ('jugada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juego.jugada')),
            ],
        ),
    ]
