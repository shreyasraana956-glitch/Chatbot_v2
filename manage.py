#!/usr/bin/env python
import os
import sys


def main():
    """Run administrative tasks."""
    # We point to the settings inside the ai_teacher subfolder
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ai_teacher.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Add the ai_teacher directory to sys.path so it can find things correctly
    sys.path.append(os.path.join(os.path.dirname(__file__), "ai_teacher"))

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
