# Generated by Django 4.0.1 on 2022-01-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('City', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='house',
            field=models.CharField(max_length=10),
        ),
    ]
