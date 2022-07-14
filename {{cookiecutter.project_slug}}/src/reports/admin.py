from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from app.base.admin import BaseModelAdmin
from reports.models import Report


@admin.register(Report)
class ReportAdmin(BaseModelAdmin):
    fieldsets = (
        (
            _('Names'),
            {
                'fields': (
                ),
            },
        ),
    )

    readonly_fields = []
    autocomplete_fields = []

    list_display = [
        'id',
        '__str__',
    ]
    list_display_links = [
        'id',
        '__str__',
    ]

    list_filter = []
    search_fields = []

    ordering = ['-id']
