# Generated by Django 5.1.6 on 2025-02-16 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typingapp', '0002_alter_favorite_id_alter_history_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='history',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
