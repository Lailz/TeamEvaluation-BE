# Generated by Django 4.0.4 on 2022-04-21 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0005_semester_created_at_semester_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='weight',
            field=models.IntegerField(default=20, max_length=100),
            preserve_default=False,
        ),
    ]