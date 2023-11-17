from django.shortcuts import render
from rest_framework import viewsets 
from .models import Singer , Song 
from .serializer import SingerSerializer , SongSerializer , Singer_Song

# Create your views here.


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    # permission_classes = []

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classeSong
class Song_SingerViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = Singer_Song
    # permission_classeSong


