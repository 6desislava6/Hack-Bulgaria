from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Projection


def index(request):
    movies = Movie.objects.all()
    projections = Projection.objects.all()
    return render(request, 'index.html', locals())


def about(request):
    return HttpResponse('About!')
