from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    # output show form
    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # create Flight table
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    # CASCADE :: table link to other table the delete will link too.
    # related_name :: which gives us a way to search for all flights 
    # with a given airport as their origin or destination.
    # is going to be a way of me accessing a relationship in the reverse order. That from a flight,
    # I can take a flight and say (.origin) to get the flight's origin in airport.
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    # output show form
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    def __str__(self):
        return f"{self.first} {self.last}"







