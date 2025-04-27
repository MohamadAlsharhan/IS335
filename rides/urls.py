from django.urls import path
from .views import request_ride, accept_ride ,ride_list , get_drivers

urlpatterns = [
    path('request_ride/', request_ride),
    path('accept_ride/', accept_ride),
    path('ride_list/', ride_list),
    path('drivers/', get_drivers),  

]