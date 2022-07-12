from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from app.base.admin import BaseModelAdmin
from products.models import Product


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    fieldsets = (
        (
            _('Names'),
            {
                'fields': (
                    'title',
                    'cost',
                    'price',
                    'count',
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
