import sys

from django.core.management.commands.makemigrations import Command as BaseCommand


class Command(BaseCommand):
    """
    Disable automatic names for django migrations,
    thanks https://adamj.eu/tech/2020/02/24/how-to-disallow-auto-named-django-migrations/
    """
    def handle(self, *args, **options):
        is_safe_run = any([options['dry_run'], options['check_changes']])

        if not options['name'] and not is_safe_run:
            message = self.style.ERROR('Migration name is required (-n/--name).')
            self.stdout.write(message)
            sys.exit(1)

        super().handle(*args, **options)
