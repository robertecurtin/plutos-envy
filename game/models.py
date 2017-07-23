from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=128, unique=True)
    order = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    city = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Unit, self).save(*args, **kwargs)

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

    def add_unit(self, unit):
        self.units[unit.name] = unit
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

    def __str__(self):
        return self.name

    
