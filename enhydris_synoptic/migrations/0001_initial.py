import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("enhydris", "0005_remove_alt_fields")]

    operations = [
        migrations.CreateModel(
            name="SynopticGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "slug",
                    models.SlugField(
                        help_text="Identifier to be used in URL", unique=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SynopticGroupStation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveSmallIntegerField()),
                (
                    "station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="enhydris.Station",
                    ),
                ),
                (
                    "synoptic_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="enhydris_synoptic.SynopticGroup",
                    ),
                ),
            ],
            options={"ordering": ["synoptic_group", "order"]},
        ),
        migrations.CreateModel(
            name="SynopticTimeseries",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveSmallIntegerField()),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Used as the chart title and as the time series title in "
                            "the report. Leave empty to use the time series name."
                        ),
                        max_length=50,
                    ),
                ),
                (
                    "subtitle",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "If time series are grouped, this is shows in the legend "
                            "of the chart and in the report, in brackets."
                        ),
                        max_length=50,
                    ),
                ),
                (
                    "default_chart_min",
                    models.FloatField(
                        blank=True,
                        help_text=(
                            "Minimum value of the y axis of the chart. If the variable "
                            "goes lower, the chart will automatically expand. If "
                            "empty, the chart will always expand just enough to "
                            "accomodate the value."
                        ),
                        null=True,
                    ),
                ),
                (
                    "default_chart_max",
                    models.FloatField(
                        blank=True,
                        help_text=(
                            "Maximum value of the y axis of the chart. If the variable "
                            "goes lower, the chart will automatically expand. If "
                            "empty, the chart will always expand just enough to "
                            "accomodate the value."
                        ),
                        null=True,
                    ),
                ),
                (
                    "group_with",
                    models.ForeignKey(
                        blank=True,
                        help_text=(
                            "Specify this field if you want to group this time series "
                            "with another in the same chart and in the report."
                        ),
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="enhydris_synoptic.SynopticTimeseries",
                    ),
                ),
                (
                    "synoptic_group_station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="enhydris_synoptic.SynopticGroupStation",
                    ),
                ),
                (
                    "timeseries",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="enhydris.Timeseries",
                    ),
                ),
            ],
            options={
                "ordering": ["synoptic_group_station", "order"],
                "verbose_name_plural": "Synoptic timeseries",
            },
        ),
        migrations.AddField(
            model_name="synopticgroupstation",
            name="timeseries",
            field=models.ManyToManyField(
                through="enhydris_synoptic.SynopticTimeseries", to="enhydris.Timeseries"
            ),
        ),
        migrations.AddField(
            model_name="synopticgroup",
            name="stations",
            field=models.ManyToManyField(
                through="enhydris_synoptic.SynopticGroupStation", to="enhydris.Station"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="synoptictimeseries",
            unique_together=set(
                [
                    ("synoptic_group_station", "timeseries"),
                    ("synoptic_group_station", "order"),
                ]
            ),
        ),
        migrations.AlterUniqueTogether(
            name="synopticgroupstation",
            unique_together=set([("synoptic_group", "order")]),
        ),
    ]
