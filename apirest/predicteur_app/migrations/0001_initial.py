# Generated by Django 3.0.2 on 2020-01-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sys', models.FloatField()),
                ('active', models.FloatField()),
                ('reassignment_count', models.FloatField()),
                ('reopen_count', models.FloatField()),
                ('sys_mod_count', models.FloatField()),
                ('made_sla', models.FloatField()),
                ('impact', models.FloatField()),
                ('urgency', models.FloatField()),
                ('priority', models.FloatField()),
                ('knowledge', models.FloatField()),
                ('time_completion', models.FloatField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
