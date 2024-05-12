# Uncomment the following imports before adding the Model code

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# from django.utils.timezone import now

# Create your models here.


# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=20)

    def __str__(self):
        template = "{0.Name} {0.Description}"
        return template.format(self)


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


class CarModel(models.Model):
    """Class representing a CarModels"""
    choice = [
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "WAGON"),
        ("Van", "Van"),
        ("Sports Car", "Sports Car"),
        ("Truck", "Truck"),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    year = models.IntegerField(
        default=2023, validators=[MaxValueValidator(2023),
                                  MinValueValidator(2015)
                                  ]
    )
    type = models.CharField(max_length=10, choices=choice, default="SUV")

    def __str__(self):
        return str(self.name)  # Return the name as the string representation
