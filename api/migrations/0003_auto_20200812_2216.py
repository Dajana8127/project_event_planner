# Generated by Django 3.0 on 2020-08-12 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rsvp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvps', to='api.Event'),
        ),
    ]
