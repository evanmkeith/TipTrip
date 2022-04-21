# Generated by Django 4.0.4 on 2022-04-21 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_profile_vehicle_model_alter_profile_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contacts',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_contact', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fee',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ratings',
            field=models.ManyToManyField(blank=True, to='main_app.rating'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='requests',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main_app.request'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vehicle_make',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vehicle_model',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Sports Car', 'Sports Car'), ('Station Wagon', 'Station Wagon'), ('Hatchback', 'Hatchback'), ('Convertible', 'Convertible'), ('SUV', 'SUV'), ('Minivan', 'Minivan'), ('Truck', 'Truck')], max_length=15),
        ),
        migrations.AlterField(
            model_name='rating',
            name='comment',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
