from django.db import models
from django.template.defaultfilters import slugify
from game.gamelog import game_log

# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=128, unique=True)
    currentCity = models.CharField(max_length=128)
    targetCity = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    owner = models.CharField(max_length=128)
    alive = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Unit, self).save(*args, **kwargs)

    def recieve_orders(self, city):
        # Prepare to move to the specified city
        self.targetCity = city

    def execute_orders(self):
        # Move the the specified city if one was selected
        if self.targetCity != '':
            game_log('{}[{}], is marching from {} to {}!'.format(\
                self.name, self.owner, self.currentCity, self.targetCity))
            newCity = City.objects.get(slug=self.targetCity)
            self.currentCity = self.targetCity
            self.targetCity = ''

    def die(self):
        # This seems like poor design but idk
        self.alive == False
        game_log('{}, controlled by {}, has died at {}'.format(self.name, self.owner, self.currentCity))
        city = City.objects.get(slug=self.currentCity)
        owner = Player.objects.get(slug=self.owner)
        city.remove_unit(self)
        owner.remove_unit(self)
        self.currentCity = 'Graveyard'

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    owner = models.CharField(max_length=128)
    units = {}
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def change_control(self, newOwner):
        game_log('{} has seized control of {} from {}'.format(newOwner, self.name, self.owner))
        self.owner = newOwner

    def add_unit(self, unit):
        self.units[unit.name] = unit

    def remove_unit(self, unit):
        self.units.pop(unit.name, None)

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

    def remove_unit(self, unit):
        self.units.pop(unit.name, None)

    def __str__(self):
        return self.name

    
