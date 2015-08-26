#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dc_campaign_finance_data_processor.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
