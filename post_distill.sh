#!/bin/bash
# Shell script to run both distill and CNAME preservation
# For Mac/Linux users

echo "Running Django Distill..."
python manage.py distill-local docs --force --collectstatic

echo "Creating CNAME file in docs directory..."
echo -n "oxfordconsultantsgh.com" > docs/CNAME

echo "Process complete!"