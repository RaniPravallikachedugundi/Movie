from django.shortcuts import render
from filmapp.models import Movie
def details(request):
    movie=Movie.objects.all()
    context={
        'movie':movie,
    }
    return render(request,'home.html',context)