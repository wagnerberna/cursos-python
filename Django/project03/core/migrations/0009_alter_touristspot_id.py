# Generated by Django 4.0.5 on 2022-06-19 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_touristspot_address_touristspot_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]