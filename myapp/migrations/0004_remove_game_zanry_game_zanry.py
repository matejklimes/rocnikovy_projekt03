# Generated by Django 4.2 on 2023-06-22 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_developer_options_alter_game_pocet_hodin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='zanry',
        ),
        migrations.AddField(
            model_name='game',
            name='zanry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.genre', verbose_name='Žánry'),
        ),
    ]
