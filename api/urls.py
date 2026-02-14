from django.urls import path 
from .serializers import RoomsSerializer
from .views import  RoomCreateApiView, RoomApiView, RoomRetrieveApiView, RoomDestroyApiView, RoomUpdateApiView


urlpatterns = [
    path('retrieve/<int:pk>', RoomRetrieveApiView.as_view(), name='retrieve'),
    path('create/<int:pk>', RoomCreateApiView.as_view(), name='create'),
    path('', RoomApiView.as_view(), name='list'),
    path('destroy/<int:pk>', RoomDestroyApiView.as_view(), name='destroy'),
    path('update/<int:pk>', RoomUpdateApiView.as_view(), name='update')
]
