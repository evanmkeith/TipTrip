# Generated by Django 4.0.4 on 2022-04-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_profile_contacts_alter_profile_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='num_seats',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
