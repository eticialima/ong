# Generated by Django 4.2.2 on 2024-07-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_blocos_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocos',
            name='conteudo',
            field=models.ManyToManyField(blank=True, to='pages.conteudo'),
        ),
    ]