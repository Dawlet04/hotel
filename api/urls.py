from django.urls import path 
from .serializers import RoomsSerializer
from .views import RoomApiView


urlpatterns = [
    path('',RoomApiView.as_view(), name = 'home')
]