from django.db import models
from django.template.defaultfilters import slugify
from game.gamelog import game_log

# Note that all handle functions slugify to allow either name or slug input
def GetCityHandle(targetName):
    return City.objects.get(slug=slugify(targetName))

def GetUnitHandle(targetName):
    return Unit.objects.get(slug=slugify(targetName))

def GetPlayerHandle(targetName):
    return Player.objects.get(slug=slugify(targetName))

# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=128, unique=True)
    currentCity = models.CharField(max_length=128)
    targetCity = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    owner = models.CharField(max_length=128)
    alive = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Unit, self).save(*args, **kwargs)

    def recieve_orders(self, city):
        # Prepare to move to the specified city
        self.targetCity = city
        self.save()

    def execute_orders(self):
        # Move the the specified city if one was selected
        if self.targetCity != '' and self.targetCity != self.currentCity:
            game_log('{}[{}], is marching from {} to {}!'.format(\
                self.name, self.owner, self.currentCity, self.targetCity))
            self.currentCity = self.targetCity
        self.save()

    def die(self):
        # This seems like poor design but idk
        self.alive == False
        game_log('{}, controlled by {}, has died at {}'.format(self.name, self.owner, self.currentCity))
        city = GetCityHandle(self.currentCity)
        owner = GetPlayerHandle(self.owner)
        owner.remove_unit(self)
        self.currentCity = 'Graveyard'
        self.save()

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    owner = models.CharField(max_length=128)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def change_control(self, newOwner):
        game_log('{} has seized control of {} from {}'.format(newOwner, self.name, self.owner))
        self.owner = newOwner
        self.save()

    def get_attackers(self):
        attackers = Unit.objects.filter(currentCity=self.name).exclude(owner=self.owner)
        attackers = [x.name for x in attackers]
        game_log('{} attackers: {}'.format(self.name, attackers))
        return attackers

    def get_defenders(self):
        defenders = Unit.objects.filter(currentCity=self.name, owner=self.owner)
        defenders =  [x.name for x in defenders]
        game_log('{} defenders: {}'.format(self.name, defenders))
        return defenders

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    units = {}

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Player, self).save(*args, **kwargs)

    def add_unit(self, unit):
        self.units[unit.name] = unit
        self.save()

    def remove_unit(self, unit):
        self.units.pop(unit.name, None)
        self.save()

    def __str__(self):
        return self.name

    
