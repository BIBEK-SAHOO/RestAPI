from django.shortcuts import render
from rest_framework import viewsets
from .models import Movies,Genre
from .serializers import MoviesSerializer,GenreSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class MovieList(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter)
    ordering = ('name')
    search_fields = ('name',)

class GenreList(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


def home(request):
    return render(request,'home.html')