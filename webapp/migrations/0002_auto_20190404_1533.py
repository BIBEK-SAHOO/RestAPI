# Generated by Django 2.0.2 on 2019-04-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='imdb_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
    ]
