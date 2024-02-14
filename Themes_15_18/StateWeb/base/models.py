from django.db import models

# Create your models here.

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    area = models.PositiveIntegerField()
    population = models.PositiveIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Human(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_birth = models.DateField()
    place_residence = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"
