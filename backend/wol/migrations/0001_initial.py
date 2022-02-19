# Generated by Django 4.0.2 on 2022-02-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(default='Unknown', max_length=100)),
                ('ip', models.GenericIPAddressField()),
                ('mac', models.CharField(max_length=17)),
                ('netmask', models.CharField(default='255.255.255.0', max_length=15)),
                ('scheduled_wake', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_notifications', models.BooleanField(default=True)),
                ('enable_console_logging', models.BooleanField(default=False)),
                ('sort_by', models.SlugField(default='name')),
                ('scan_address', models.GenericIPAddressField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Websocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitors', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
