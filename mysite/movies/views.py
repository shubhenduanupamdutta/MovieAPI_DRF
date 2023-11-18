# from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MovieSerializer
from .models import MovieData
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all().order_by('id')
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='action').order_by('id')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='comedy').order_by('id')
    serializer_class = MovieSerializer
