#!/bin/bash

# This script starts the application

python manage.py runserver 0.0.0.0:"$PORT"
