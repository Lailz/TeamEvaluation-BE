# Generated by Django 4.0.4 on 2022-04-20 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team_app.semester'),
        ),
    ]
