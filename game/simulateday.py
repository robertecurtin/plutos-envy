from game.models import Unit, City, Player
from game.gamelog import game_log

def simulate_day():
    # This handles all end-of-day events and cleanup
    # First, we move all units to their requested destination
    for unit in Unit.objects.all():
       unit.execute_orders()
       
    # Next, we handle each city's battle
    for city in City.objects.all():
        # We start by separating the units into attackers and defenders
        # Most of the time, units will be defenders, so it is easiest to assume all
        # units are defenders and check which units are actually attackers
        attackers = {}
        defenders = city.units
        for unitName, unit in defenders:
            if unit.owner != city.owner:
                attackers.append(defenders.pop(unitName))

        # Next, we remove attackers and defenders until one side is depleted
        while attackers != {} and defenders != {}:
            game_log('A battle has begun at {}!'.format(city.name))
            simulate_battle(attackers, defenders, city)
        # If the attackers won, they gain control of the city.
        # If the defenders won or tied, they retain control.
        if attackers != {}:
            # This doesn't handle simultaneous attacks yet
            # It is also super inefficient
            newOwner = ''
            for attacker in attackers:
                newOwner = attacker.owner
            city.change_control(newOwner)
        else:
            game_log('The defenders have held their ground.')
                



    

def simulate_battle(attackers, defenders, city):
    # For the initial version, we will simply kill one attacker and defender per battle.
    attacker = attackers.pop()
    defender = defenders.pop()
    attacker.die()
    defender.die()
