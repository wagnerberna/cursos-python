# Generated by Django 4.1.1 on 2022-09-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("helpdesk", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="demand",
            name="title",
            field=models.CharField(max_length=70, null=True),
        ),
    ]