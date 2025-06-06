# Generated by Django 5.2 on 2025-04-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rides", "0002_remove_ride_estimated_price_remove_ride_status_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ride",
            name="end_time",
        ),
        migrations.AddIndex(
            model_name="ride",
            index=models.Index(fields=["driver"], name="rides_ride_driver__850520_idx"),
        ),
        migrations.AddIndex(
            model_name="ride",
            index=models.Index(
                fields=["start_time"], name="rides_ride_start_t_3fc3ef_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="ride",
            index=models.Index(fields=["rider"], name="rides_ride_rider_i_0b8823_idx"),
        ),
    ]
