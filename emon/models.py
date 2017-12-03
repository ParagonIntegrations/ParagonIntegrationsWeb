from django.db import models
from django.urls import reverse  # Used to generate urls by reversing the URL patterns
import uuid


class Installation(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, help_text="Enter the address of this installation")
    name = models.CharField(max_length=200, help_text="Enter a descriptive name for this installation")


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Name

class Meter(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    id = models.IntegerField(primary_key=True, help_text="ID of the meter")
    serial = models.CharField(max_length= 200,unique=True)
    num_channels = models.PositiveSmallIntegerField()
    installation_date = models.DateField()
    installation = models.ForeignKey('Installation')


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id

class Channel(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    id = models.CharField(max_length=200, help_text="Channel ID(consists of meter ID and channel number")
    meter = models.ForeignKey('Meter')


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id

class ChannelData(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    timestamp = models.DateTimeField()
    vrms = models.DecimalField(max_digits=5, decimal_places=2)
    irms = models.DecimalField(max_digits=5, decimal_places=2)
    units_left = models.DecimalField(max_digits=10, decimal_places=6)
    unitsused = models.DecimalField(max_digits=8, decimal_places=6)
    unit_counter = models.DecimalField(max_digits=13, decimal_places=6)
    description = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name