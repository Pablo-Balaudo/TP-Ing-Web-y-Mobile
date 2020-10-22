# Generated by Django 3.1 on 2020-10-15 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Foro', '0003_denunciacomment_denunciapost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_posted']},
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                    to='Foro.post'),
        ),
    ]
