#!/bin/bash
# Run this after making database changes
python3 manage.py makemigrations game
python3 manage.py migrate
python3 populate_game.py
