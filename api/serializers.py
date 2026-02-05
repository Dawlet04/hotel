from rest_framework import routers, serializers, 
from hotelsapp.models import Room, Booking, Hotel


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        