# Generated by Django 2.2.7 on 2019-11-21 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enhydris", "0025_gentity_geom"),
        ("enhydris_synoptic", "0004_limits"),
    ]

    operations = [
        migrations.AddField(
            model_name="synopticgroup",
            name="time_zone",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="enhydris.TimeZone",
            ),
            preserve_default=False,
        )
    ]
