# Generated by Django 5.0.1 on 2024-04-15 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_hotelbook_checkin_alter_hotelbook_checkout_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotelbook',
            options={'verbose_name_plural': 'Hotel Bookings'},
        ),
        migrations.AlterModelOptions(
            name='tickbooking',
            options={'verbose_name_plural': 'Ticket Bookings'},
        ),
        migrations.AlterModelTable(
            name='hotelbook',
            table=None,
        ),
        migrations.AlterModelTable(
            name='tickbooking',
            table=None,
        ),
    ]
