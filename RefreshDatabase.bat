#!/bin/bash
# Run this after making database changes.
# To perform a hard reset, rerun InitializeSetup.bat.
python3 manage.py makemigrations game
python3 manage.py migrate
python3 populate_game.py
