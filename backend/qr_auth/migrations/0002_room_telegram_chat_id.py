# Generated by Django 5.2.4 on 2025-07-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='telegram_chat_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
