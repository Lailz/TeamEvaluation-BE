# Generated by Django 4.0.4 on 2022-04-22 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0015_alter_project_slug_alter_team_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='teams',
        ),
        migrations.AddField(
            model_name='team',
            name='teams',
            field=models.ManyToManyField(to='team_app.project'),
        ),
    ]