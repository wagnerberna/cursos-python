# Generated by Django 4.0.5 on 2022-06-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attraction',
            fields=[
                ('id_attraction', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('opening_hours', models.TimeField()),
                ('closing_hours', models.TimeField()),
                ('minimum_age', models.IntegerField()),
            ],
            options={
                'db_table': 'attraction',
                'managed': True,
            },
        ),
    ]
