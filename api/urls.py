from django.urls import path 
from .serializers import RoomsSerializer
from .views import RoomApiView, RoomCreateApiView, RoomRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('',RoomApiView.as_view(), name = 'home'),
    path('create/', RoomCreateApiView.as_view(), name='create'),
    path('<int:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view(), name = 'complex')
]