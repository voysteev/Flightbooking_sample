from django.db import models

# Create your models here.

class airports(models.Model):
    code = models.CharField(max_length=3)
    airport=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code}:{self.airport}"

class Flight(models.Model):
    origin = models.ForeignKey(airports,on_delete=models.CASCADE,related_name='departures') #models.CharField(max_length=100)
    destination = models.ForeignKey(airports,on_delete=models.CASCADE,related_name='arrivals')#models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination} in {self.duration} mins."

class Passenger(models.Model):
    first=models.CharField(max_length=100)
    last=models.CharField(max_length=100)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

'''
python3 manage.py makemigrations
python3 manage.py makemigrations
python manage.py shell
from flights.models import *
>>> jfk=airports(code="NYC",airport="New York")
>>> jfk.save()
>>> lhr=airports(code="LND",airport="London")
>>> lhr.save()
>>> pqr=airports(code="PRS",airport="Paris")
>>> pqr.save()
>>> lmn=airports(code="TOK",airport="Tokyo")
>>> lmn.save()
>>> f= Flight(origin=jfk,destination=lhr,duration=423) ---->objects are passed as foreign key
>>> f.save() ---> saving flight object dont forget ****
>>> f
<Flight: None:NYC:New York to LND:London in 423 mins.>
>>> f.origin
>>> jfk.departures.all() ----> related name to get all departures from jfk airport


ADDING MORE DATA LATER AFTER CREATING FOREIGN KEY TABLE WE DO NOT REQUIRE TO CREATE AIRPORT OBJECTS AGAIN JUST DIRECTLY IMPORT MODELS AND CREATE FLIGHT OBJECTS

from flights.models import *
>>> airports.objects.all()
<QuerySet [<airports: NYC:New York>, <airports: LND:London>, <airports: PRS:Paris>, <airports: TOK:Tokyo>, <airports: NYC:New York>, <airports: LND:London>]>
>>> airports.objects.filter(airport="Paris")
<QuerySet [<airports: PRS:Paris>]>
>>> airports.objects.filter(airport="Paris").first()
<airports: PRS:Paris>
>>> obj1=airports.objects.get(airport="Paris") -->get only gives single object if multiple it will give error
>>> obj2=airports.objects.get(airport="London")
>>> obj3=Flight(origin=obj1,destination=obj2,duration=768)
>>> obj3.save()

REGISTERING MODELS IN ADMIN.PY

'''