# Generated by Django 5.1.7 on 2025-05-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_alter_filme_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens/%Y/%m/'),
        ),
    ]
