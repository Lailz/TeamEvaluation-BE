# Generated by Django 4.0.4 on 2022-04-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0009_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='teams',
            field=models.ManyToManyField(to='team_app.team'),
        ),
    ]
