from django.urls import path 
from .serializers import RoomsSerializer
from .views import  RoomCreateApiView, RoomRetrieveUpdateDestroyAPIView, RoomApiView


urlpatterns = [
    
    path('create/', RoomCreateApiView.as_view(), name='create'),
    path('<int:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view(), name = 'complex'),
    path('', RoomApiView.as_view(), name='list'),
]