# Generated by Django 3.1 on 2020-09-25 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Juego', '0007_auto_20200925_1559'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='color',
            unique_together=set(),
        ),
    ]
