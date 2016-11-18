#!/usr/bin/env python
import os
import sys

# Make project directory available for imports.
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "project"))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scifight_heroku_settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
