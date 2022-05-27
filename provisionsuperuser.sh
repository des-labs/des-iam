#!/bin/bash

ERR_MSG="$(python3 manage.py createsuperuser --no-input 2>&1 > /dev/null)"
if [[ "$ERR_MSG" == "" ]]; then
  echo "superuser created successfully"
  exit 0
fi
if [[ "$ERR_MSG" == "CommandError: Error: That username is already taken." ]]; then
  echo "superuser already exists"
  exit 0
fi
echo "$ERR_MSG"
exit 1
