from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from .serializers import RoomsSerializer
from hotelsapp.models import Room, Booking, Hotel


class RoomApiView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomsSerializer 


