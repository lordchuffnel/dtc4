from datetime import datetime
import pandas as pd
from django.contrib import admin
from django.http import HttpResponse

from .models import Timecard


class ExportCsvMixin:
    def get_model_field_names(self, model):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        return field_names

    def get_lookup_fields(self, model, fields=None):
        model_field_names = self.get_model_field_names(model)
        if fields is not None:
            for obj in fields:
                lookup_fields = [getattr(obj, field) for field in fields]
        else:
            lookup_fields = model_field_names
        return lookup_fields

    def qs_to_dataset(self, qs, fields=None):
        lookup_fields = self.get_lookup_fields(qs.model, fields=fields)
        return list(qs.values(*lookup_fields))

    def convert_to_dataframe(self, qs, fields=None, index=None):
        lookup_fields = self.get_lookup_fields(qs.model, fields=fields)
        index_col = None
        if index in lookup_fields:
            index_col = index
        elif "id" in lookup_fields:
            index_col = "id"
        values = self.qs_to_dataset(qs, fields=fields)
        df = pd.DataFrame.from_records(
            values, columns=lookup_fields, index=index_col,)
        return df

    def export_as_csv(self, request, queryset):

        result = self.convert_to_dataframe(queryset)
        name = result.loc[1, "user"]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}{}.csv".format(
            name, datetime.date()
        )
        result.to_csv(path_or_buf=response, sep=";",
                      float_format="%.2f", index=True)

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Timecard)
class TimecardAdmin(admin.ModelAdmin, ExportCsvMixin):
    ordering = ("-date",)
    list_display = [
        "user",
        "date",
        "start_time",
        "end_time",
        "int_hours",
        "ext_hours",
        "lunch",
        "sick_day",
        "total_hours",
    ]
    list_filter = ("user", "date")
    actions = ["export_as_csv"]

    # def show_timecard(self, obj):
    #     return '\n'.join([str(a.date) for a in obj.timecards.all()])
