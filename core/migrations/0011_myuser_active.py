# Generated by Django 5.0.1 on 2024-04-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_myuser_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
