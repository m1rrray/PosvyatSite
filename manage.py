#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#
# SPREADSHEET_ID = '1w5u-71ezRExkVrox6hX1-DNx_lEV4AJ7YdAO1b74HWs'

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PosvyatSite.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
