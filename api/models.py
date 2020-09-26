from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta




class Timecard(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, db_column="user", to_field="username"
    )
    date = models.DateField(verbose_name="Date")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
    lunch = models.BooleanField(blank=True, default=False)
    sick_day = models.BooleanField(blank=True, default=False)
    int_hours = models.DecimalField(
        verbose_name="Interior Hours",
        decimal_places=2,
        max_digits=4,
        blank=True,
        default=0,
    )
    ext_hours = models.DecimalField(
        verbose_name="Exterior Hours",
        decimal_places=2,
        max_digits=4,
        blank=True,
        default=0,
    )

    def total_hours(self):
        return self.int_hours + self.ext_hours

    def hours_validation(self):
        datetimeA = datetime.combine(date.today(), self.start_time)
        datetimeB = datetime.combine(date.today(), self.end_time)
        timediff = datetimeB - datetimeA
        thours = abs(round(timediff.total_seconds() / 3600, 2))
        if self.lunch:
            thours = thours - 0.5
            return bool(thours == (self.int_hours + self.ext_hours))
        return bool(thours == (self.int_hours + self.ext_hours))
