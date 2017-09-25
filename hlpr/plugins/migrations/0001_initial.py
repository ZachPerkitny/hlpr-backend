# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 01:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hlpr.plugins.fields
import hlpr.plugins.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Files',
                'verbose_name': 'File',
            },
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('description', models.TextField(max_length=4096)),
                ('created', models.DateTimeField(editable=False)),
                ('last_updated', models.DateTimeField()),
                ('repository', models.URLField(blank=True)),
                ('category', models.CharField(choices=[('admin_commands', 'Admin Commands'), ('fun_commands', 'Fun Commands'), ('gameplay', 'Gameplay'), ('general_purpose', 'General Purpose'), ('server_management', 'Server Management'), ('statistical', 'Statistical'), ('technical_development', 'Technical/Development')], default='general_purpose', max_length=24)),
                ('game', models.CharField(choices=[('age_of_chivalry', 'Age of Chivalry'), ('alien_swarm', 'Alien Swarm'), ('any', 'Any'), ('battlegrounds_2', 'Battlegrounds 2'), ('csgo', 'Counter-Strike: GO'), ('css', 'Counter-Strike: Source'), ('dods', 'Day of Defeat: Source'), ('day_of_infamy', 'Day of Infamy'), ('dino_d_day', 'Dino D-Day'), ('dystopia', 'Dystopia'), ('empires', 'Empires'), ('fortress_forever', 'Fortress Forever'), ('HL2DM', 'Half-Life 2 Deathmatch'), ('l4d', 'Left 4 Dead'), ('neotokyo', 'Neotokyo')], default='any', max_length=16)),
                ('mod', models.CharField(choices=[('amx_mod_x', 'AMX Mod X'), ('metamod', 'MetaMod'), ('sourcemod', 'SourceMod')], default='sourcemod', max_length=12)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plugin_author', to=settings.AUTH_USER_MODEL)),
                ('collaborators', models.ManyToManyField(related_name='plugin_collaborator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Plugins',
                'verbose_name': 'Plugin',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', hlpr.plugins.fields.VersionNumberField(default=hlpr.plugins.models.version_default)),
                ('plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='plugins.Plugin')),
            ],
            options={
                'verbose_name_plural': 'Versions',
                'verbose_name': 'Version',
            },
        ),
        migrations.AddField(
            model_name='file',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='plugins.Version'),
        ),
    ]
