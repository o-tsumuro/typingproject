# Generated by Django 4.2 on 2025-02-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0004_remove_content_play_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='play_count',
            field=models.IntegerField(default=0),
        ),
    ]
