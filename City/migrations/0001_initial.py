# Generated by Django 4.0.1 on 2022-01-11 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='City_Street', to='City.city')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('house', models.IntegerField()),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='City_Shop', to='City.city')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Street_Shop', to='City.street')),
            ],
        ),
    ]
