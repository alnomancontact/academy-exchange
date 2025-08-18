"""
WSGI config for exchange project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange.settings')

# --- Auto-run migrations on startup ---
try:
    import django
    from django.core.management import call_command

    django.setup()
    call_command("migrate", interactive=False)
    print("✅ Migrations applied successfully")
except Exception as e:
    print("⚠️ Migration skipped or failed:", e)
# --------------------------------------

# Standard WSGI application
application = get_wsgi_application()
