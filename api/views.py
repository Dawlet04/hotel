from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView,  RetrieveUpdateDestroyAPIView
from .serializers import RoomsSerializer
from hotelsapp.models import Room, Booking, Hotel

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny

# class RoomApiView(ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomsSerializer


# class RoomCreateApiView(CreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomsSerializer



class RoomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomsSerializer


class RoomApiView(APIView):
    permission_classes = [AllowAny]
    def get(self, request ):
        queryset = Room.objects.all()
        serializer = RoomsSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class RoomCreateApiView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        queryset = Room.objects.all()
        serializer = RoomsSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)





























































