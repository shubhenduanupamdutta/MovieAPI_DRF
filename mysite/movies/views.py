# from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MovieSerializer
from .models import MovieData
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all().order_by('name')
    serializer_class = MovieSerializer
