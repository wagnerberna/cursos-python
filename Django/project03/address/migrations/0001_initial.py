# Generated by Django 4.0.5 on 2022-06-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id_address', models.AutoField(primary_key=True, serialize=False)),
                ('street', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'address',
                'managed': True,
            },
        ),
    ]
