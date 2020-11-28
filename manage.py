#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from config.settings.base import root


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # This allows easy placement of apps within the interior "urbandata" directory.
    app_path = root("urbandata")
    sys.path.append(app_path)

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
