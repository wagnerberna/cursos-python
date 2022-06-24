# Generated by Django 4.0.5 on 2022-06-18 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_touristspot_address'),
        ('attraction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='id_tourist_spot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tourist_spot', to='core.touristspot'),
        ),
    ]
