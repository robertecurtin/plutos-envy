from game.models import Unit, City, Player, GetUnitHandle
from game.gamelog import game_log

def simulate_day():
    # This handles all end-of-day events and cleanup
    # First, we move all units to their requested destination
    for unit in Unit.objects.all():
       unit.execute_orders()
       
    # Next, we handle each city's battle
    for city in City.objects.all():
        # We start by separating the units into attackers and defenders
        attackers = city.get_attackers()
        defenders = city.get_defenders()
        if attackers == []:
            game_log('All quiet at {}.'.format(city.name))
            continue

        # Next, we remove attackers and defenders until one side is depleted
        while attackers != [] and defenders != []:
            game_log('A battle has begun at {}!'.format(city.name))
            simulate_battle(attackers, defenders, city)
            # If the attackers won, they gain control of the city.
            # If the defenders won or tied, they retain control.

        if attackers != []:
            # This doesn't handle simultaneous attacks yet
            # It is also super inefficientnewOwner = ''
            newOwner = ''
            for attacker in attackers:
                newOwner = attacker.owner
            city.change_control(newOwner)
        else:
            game_log('The defenders have held their ground.')
                



    

def simulate_battle(attackers, defenders, city):
    # For the initial version, we will simply kill one attacker and defender per battle.
    attacker = GetUnitHandle(attackers.pop())
    defender = GetUnitHandle(defenders.pop())
    attacker.die()
    defender.die()
