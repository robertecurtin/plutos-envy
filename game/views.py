from django.http import HttpResponse
from django.shortcuts import render
from game.models import Unit, City, Player
from game.simulateday import simulate_day
from game.gamelog import get_game_log_html
# Create your views here.
# These provide information to the html files under /templates/game, and
# call the rendering of those pages.

def simulate_day_callback(request):
    simulate_day()
    text = get_game_log_html()
    return HttpResponse(text)

def orders(request, unit_name_slug):
    return HttpResponse("Aye aye!")

def unit(request, unit_name_slug):
    context_dict = {}

    try:
        unit = Unit.objects.get(slug=unit_name_slug)
        cities = City.objects.order_by('name')
        cityNames = [city.name for city in cities]
        context_dict['city_names'] = cityNames # Used to determine destination
        context_dict['unit_name'] = unit.name.rstrip("\n\r")
        context_dict['unit_target_city'] = unit.targetCity
        context_dict['unit_owner'] = unit.owner
        context_dict['unit_current_city'] = unit.currentCity

    except Unit.DoesNotExist:
        pass
    return render(request, 'game/unit.html', context_dict)

def city(request, city_name_slug):
    context_dict = {}

    try:
        city = City.objects.get(slug=city_name_slug)
        context_dict['city_name'] = city.name
        context_dict['city_units'] = Unit.objects.filter(city=city)
        context_dict['city_owner'] = city.owner
    except City.DoesNotExist:
        pass
    return render(request, 'game/city.html', context_dict)

def player(request, player_name_slug):
    context_dict = {}
    try:
        player = Player.objects.get(slug=player_name_slug)
        context_dict['player_name'] = player.name
        context_dict['player_cities'] = City.objects.filter(owner=player)
        context_dict['player_units'] = Unit.objects.filter(owner=player)
    except Player.DoesNotExist:
        pass
    return render(request, 'game/player.html', context_dict)

def index(request):
    return HttpResponse("This is the index!")
