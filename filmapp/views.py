from django.shortcuts import get_object_or_404, render
from filmapp.models import Movie
def about_movie(request,pk):
    movie=get_object_or_404(Movie,pk=pk)
    context={
        'movie':movie,
    }
    return render(request,'about_movie.html',context)
# Create your views here.
