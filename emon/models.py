from django.db import models
from django.urls import reverse  # Used to generate urls by reversing the URL patterns
import uuid


class Installations(models.Model):
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
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('installation-detail', args=[str(self.id)])

class Meters(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    id = models.IntegerField(primary_key=True, help_text="ID of the meter")
    serial = models.CharField(max_length= 200,unique=True)
    num_channels = models.PositiveSmallIntegerField()
    installation_date = models.DateField()
    installation = models.ForeignKey('Installations', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id

class Channels(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    id = models.IntegerField(primary_key=True, help_text="Channel ID(consists of meter ID and channel number")
    meter = models.ForeignKey('Meters', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id

class ChannelData(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    channel = models.ForeignKey('Channels', on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField()
    vrms = models.DecimalField(max_digits=5, decimal_places=2)
    irms = models.DecimalField(max_digits=5, decimal_places=2)
    units_left = models.DecimalField(max_digits=10, decimal_places=6)
    unitsused = models.DecimalField(max_digits=8, decimal_places=6)
    unit_counter = models.DecimalField(max_digits=13, decimal_places=6)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.timestamp