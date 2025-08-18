# render_migrate.py
import os
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exchange.settings")
django.setup()

# Run migrations
call_command("migrate", interactive=False)
