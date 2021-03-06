# Generated by Django 3.0.7 on 2020-06-16 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Timecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('lunch', models.BooleanField(blank=True, default=False)),
                ('sick_day', models.BooleanField(blank=True, default=False)),
                ('int_hours', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, verbose_name='Interior Hours')),
                ('ext_hours', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, verbose_name='Exterior Hours')),
                ('user', models.ForeignKey(db_column='user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
