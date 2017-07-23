# plutos-envy
Attempt to make a strategy game where players only make moves on an hourly or daily basis. Inspired by Neptune's Pride.

## Setup
The project is built using Python 3.4.2 and Django 1.11.3. I am running this on a Raspberry Pi 3.
Currently, the project runs on a local server. Use "python3 manage.py runserver" to start the local server.
Run InitialSetup.sh to set up the database and create an admin account.

## Link Organization
/game/player/<player-name>
    Provides information about the named player
/game/city/<city-name>
    Provides information about the named city
/game/unit/<unit-name>
    Provides information about the named unit

### LAN server setup
If you want to run the server on one computer and connect from other computers on the network, use RunServer.bat.
Note that you will need to update ALLOWED_HOSTS under PlutosEnvy/settings.py with your internal IP address.
