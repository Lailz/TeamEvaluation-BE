# Generated by Django 4.0.4 on 2022-04-22 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0012_alter_project_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='team_app.semester'),
        ),
    ]
