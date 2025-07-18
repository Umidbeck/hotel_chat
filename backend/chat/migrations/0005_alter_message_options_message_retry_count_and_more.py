# Generated by Django 5.2.4 on 2025-07-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_message_uuid'),
        ('qr_auth', '0003_alter_room_check_in_alter_room_check_out_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['sent_at']},
        ),
        migrations.AddField(
            model_name='message',
            name='retry_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('delivered', 'Delivered'), ('failed', 'Failed')], default='pending', max_length=10),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['chatroom', 'status'], name='chat_messag_chatroo_e82375_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['uuid'], name='chat_messag_uuid_557b32_idx'),
        ),
    ]
