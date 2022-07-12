from os import path

from django.conf import settings
from django.core.management.commands.startapp import Command as BaseCommand


class Command(BaseCommand):
    """
    Force using custom app template for all newly created apps.
    Should be provided with both app name and main model name.
    Example: ./manage.py startapp products Product
    """

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('model', action='store', type=str)

    def handle(self, **options):
        options['template'] = path.join(settings.BASE_DIR, '.app-template')
        super().handle(**options)
