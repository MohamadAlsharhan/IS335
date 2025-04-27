from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from .models import Ride, Driver



@api_view(['POST'])
def request_ride(request):
    print("Request Data:", request.data)  # Debugging output
    if 'rider_id' not in request.data:
        return Response({'error': 'Missing rider_id'}, status=400)

    with transaction.atomic():
        ride = Ride.objects.create(rider_id=request.data['rider_id'])
        return Response({'message': 'Ride requested', 'ride_id': ride.id})
    
    
@api_view(['POST'])
def accept_ride(request):
    print("Request Data:", request.data)  # Debugging output
    if 'ride_id' not in request.data:
        return Response({'error': 'Missing ride_id'}, status=400)

    with transaction.atomic():
        ride = Ride.objects.filter(id=request.data['ride_id'], status='pending').first()
        if not ride:
            return Response({'error': 'Ride not found or already accepted'}, status=400)

        try:
            driver = Driver.objects.get(id=request.data['driver_id'])
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=404)

        ride.driver = driver
        ride.status = 'accepted'
        ride.save()
        return Response({'message': 'Ride accepted!', 'ride_id': ride.id, 'driver': driver.name})



@api_view(['GET'])
def ride_list(request):
    """Retrieve all requested and accepted rides."""
    requested_rides = Ride.objects.filter(status='pending').values('id', 'rider_id', 'start_time')
    accepted_rides = Ride.objects.filter(status='accepted').values('id', 'rider_id', 'driver_id', 'start_time')

    return Response({
        "requested_rides": list(requested_rides),
        "accepted_rides": list(accepted_rides)
    })

@api_view(['GET'])
def get_drivers(request):
    drivers = Driver.objects.values('id', 'name')
    return Response({"drivers": list(drivers)})




'''
@api_view(['POST'])
def request_ride(request):
    """Handles ride requests"""
    with transaction.atomic():  # Ensures atomicity
        ride = Ride.objects.create(rider_id=request.data['rider_id'])
        return Response({'message': 'Ride requested', 'ride_id': ride.id})

@api_view(['POST'])
def accept_ride(request):
    """Handles ride acceptances"""
    with transaction.atomic():
        ride = Ride.objects.filter(id=request.data['ride_id'], status='pending').first()
        if not ride:
            return Response({'error': 'Ride not found or already accepted'}, status=400)

        try:
            driver = Driver.objects.get(id=request.data['driver_id'])
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=404)

        ride.driver = driver
        ride.status = 'accepted'
        ride.save()
        return Response({'message': 'Ride accepted!', 'ride_id': ride.id, 'driver': driver.name})
    '''


#from rides.models import Rider, Driver, Vehicle

#rider1 = Rider.objects.create(name="Mohammed", email="mohammed@example.com", phone="1234567890")
#driver1 = Driver.objects.create(name="Ali", email="ali@example.com", phone="0987654321", license_nb="XYZ123")
#vehicle1 = Vehicle.objects.create(make="Toyota", model="Camry", color="Black", plate_nb="ABC123", driver=driver1)
