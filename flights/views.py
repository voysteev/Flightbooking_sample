from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,"flights/index.html",{
        "flights":Flight.objects.all()
    })

def flight(request, flight_id):
    flight=Flight.objects.get(pk=flight_id)#or id=flight_id
    # if not flight:
    #     return render(request,"flights/errors.html",{
    #         'error':'Flight does not exist'
    #     })
        
    return render(request,"flights/flight.html",{
        'flight':flight,
        "passengers":flight.passengers.all(),        #where passengers is related name in models.
        "non_passengers":Passenger.objects.exclude(flights=flight).all()#--->to be able to add passengers who are not in this flight already
    })

def book(request, flight_id):
    if request.method=="POST":
        flight=Flight.objects.get(pk=flight_id)
        PK=int(request.POST["passenger"])#--->this passenger is name attribute in html form in flight.html
        passenger=Passenger.objects.get(pk=PK)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight',args=(flight.id,)))#---->the comma is important to make it a tuple
