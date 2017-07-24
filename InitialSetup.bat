#!/bin/bash
python3 manage.py flush --noinput # Unnecessary on the first run, but allows a hard reset otherwise
python3 manage.py migrate
python3 manage.py makemigrations game
python3 manage.py migrate
python3 manage.py createsuperuser
python3 populate_game.py
