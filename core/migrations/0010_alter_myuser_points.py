# Generated by Django 5.0.1 on 2024-04-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_myuser_points_delete_userpoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
