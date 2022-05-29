# Generated by Django 4.0.4 on 2022-05-29 11:28

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_linguagem_professor_projeto_cadeira'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='ano_letivo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='projeto',
            name='disciplina',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='projeto',
            name='tecnologias',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(upload_to=portfolio.models.posts_resolution_path),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
