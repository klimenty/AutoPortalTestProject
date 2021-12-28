from django.db import models
# Added import
from django.urls import reverse  # To generate URLS by reversing URL patterns
from datetime import date


# from django.contrib.auth.models import User #For future user implementation


# Create your models here.
class LowerCharField(models.CharField):
    """
    Transform text to lowercase for BD columns and rows, where data must be unique.
    """

    def __init__(self, *args, **kwargs):
        super(LowerCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Car(models.Model):
    """
    Model representing a car (but not a specific copy of a car).
    """
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because car can only have one manufacturer, but manufacturers can have multiple cars
    # Manufacturer as a string rather than object because it hasn't been declared yet in file.
    car_model = models.ForeignKey('CarModel', on_delete=models.SET_NULL, null=True, help_text="Select a car model")
    car_color = models.ForeignKey('CarColor', on_delete=models.SET_NULL, null=True, help_text="Select a car color")

    class Meta:
        ordering = ['manufacturer', 'car_model', 'car_color']

    # def display_manufacturer(self):
    #     """Creates a string for the Manufacturer. This is required to display genre in Admin."""
    #     return ', '.join([manufacturer.name for manufacturer in self.manufacturer.all()[:3]])

    # display_manufacturer.short_description = 'Manufacturer'

    def get_absolute_url(self):
        """Returns the url to access a particular car instance."""
        return reverse('car-detail', args=[str(self.vin)])

    def __str__(self):
        """String for representing the Model object."""
        return '{}'.format(self.car_model)


class CarInstance(models.Model):
    """Model representing a specific copy of a car."""
    vin = LowerCharField(max_length=200, default='', help_text="Unique VIN for this particular car")
    # vin must be unique. "CONSTRAINT unique_vin UNIQUE (vin)" were used to check duplicates on DB level
    car = models.ForeignKey('Car', on_delete=models.RESTRICT, null=True)
    dealer = models.ForeignKey('Dealer', on_delete=models.RESTRICT, null=True)
    date_of_arrival_to_dealer = models.DateField(null=True, blank=True)
    dealer_center = models.ForeignKey('DealerCenter', on_delete=models.RESTRICT, null=True)
    date_of_arrival_to_dealer_center = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.vin)


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
        return '{}'.format(self.name)


class CarColor(models.Model):
    """Model representing a car color (e.g. Red, Black, Green, etc.)"""
    name = models.CharField(
        max_length=200,
        help_text="Enter a car color (e.g. Red, Black, Green, etc.)"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return '{}'.format(self.name)


class Dealer(models.Model):
    """Model representing an Dealer."""
    dealer_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the url to access a particular dealer instance."""
        return reverse('dealer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.dealer_name)


class DealerCenter(models.Model):
    """Model representing an Manufacturer."""
    dealer_center_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the url to access a particular dealer center instance."""
        return reverse('dealer-center-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.dealer_center_name)
