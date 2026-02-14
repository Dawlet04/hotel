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



# class RoomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomsSerializer


class RoomApiView(APIView):
    permission_classes = [AllowAny]
    def get(self, request ):
        queryset = Room.objects.all()
        serializer = RoomsSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


class RoomRetrieveApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        room = Room.objects.get(id=pk)
        serializer = RoomsSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RoomDestroyApiView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, pk):
        room = Room.objects.get(id=pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RoomCreateApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RoomsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RoomUpdateApiView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        room = Room.objects.get(id=pk)
        serializer = RoomsSerializer(room, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
























































