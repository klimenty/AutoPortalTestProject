from django.db import models
#Added import
from django.urls import reverse #To generate URLS by reversing URL patterns
import uuid  # Required for unique car instances
from datetime import date
# from django.contrib.auth.models import User #For future user implementation


# Create your models here.
class Car(models.Model):
    """
    Model representing a car (but not a specific copy of a car).
    """
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because car can only have one manufacturer, but manufacturers can have multiple cars
    # Manufacturer as a string rather than object because it hasn't been declared yet in file.
    car_model = models.ForeignKey('Car model', on_delete=models.SET_NULL, null=True, help_text="Select a car model")
    car_color = models.ForeignKey('Car color', on_delete=models.SET_NULL, null=True, help_text="Select a car color")

    class Meta:
        ordering = ['Manufacturer', 'Car model', 'Car color']

    def display_manufacturer(self):
        """Creates a string for the Manufacturer. This is required to display genre in Admin."""
        return ', '.join([manufacturer.name for manufacturer in self.manufacturer.all()[:3]])

    display_manufacturer.short_description = 'Manufacturer'

    def get_absolute_url(self):
        """Returns the url to access a particular car instance."""
        return reverse('car-detail', args=[str(self.vin)])

    def __str__(self):
        """String for representing the Model object."""
        return self.car_model


class CarInstance(models.Model):
    """Model representing a specific copy of a car."""
    vin = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique VIN for this particular car")
    car = models.ForeignKey('Car', on_delete=models.RESTRICT, null=True)
    dealer = models.ForeignKey('Dealer', on_delete=models.RESTRICT, null=True)
    date_of_arrival_to_dealer = models.DateField(null=True, blank=True)
    dealer_center = models.ForeignKey('Dealer Center', on_delete=models.RESTRICT, null=True)
    date_of_arrival_to_dealer_center = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.vin, self.car.car_model)


class Manufacturer(models.Model):
    """Model representing an Manufacturer."""
    manufacturer_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the url to access a particular manufacturer instance."""
        return reverse('manufacturer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.manufacturer_name)


class CarModel(models.Model):
    """Model representing a car model (e.g. Duster, Vitara, SX4, etc.)"""
    name = models.CharField(
        max_length=200,
        help_text="Enter a car model (e.g. Duster, Vitara, SX4, etc.)"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class CarColor(models.Model):
    """Model representing a car color (e.g. Red, Black, Green, etc.)"""
    name = models.CharField(
        max_length=200,
        help_text="Enter a car color (e.g. Red, Black, Green, etc.)"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
