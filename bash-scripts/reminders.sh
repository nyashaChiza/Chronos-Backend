#!/bin/bash

# Activate the virtual environment
source workon chronos

# Change to the directory where your Django project is located
cd /Users/user/dev/python/Chronos/

# Run the Django management command to send event reminders
python manage.py shell -c "from evaluation.helpers import send_event_reminders; send_event_reminders()"

# Deactivate the virtual environment
deactivate