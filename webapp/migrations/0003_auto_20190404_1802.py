# Generated by Django 2.0.2 on 2019-04-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190404_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='imdb_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='popularity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
