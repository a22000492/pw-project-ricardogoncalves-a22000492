# Generated by Django 4.0.4 on 2022-06-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_tfc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfc',
            name='resumo',
            field=models.TextField(),
        ),
    ]
