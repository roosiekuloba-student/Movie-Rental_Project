from django.http import HttpResponse
from .models import Movie, MovieGenre
from django.template import loader
from django.shortcuts import render,  get_object_or_404
# Create your views here.


def index(request):
    """View function for home page of site."""
    movie_list = Movie.objects.order_by('-launch_date')
    num_movies = Movie.objects.all().count()
    # template = loader.get_template('moviecatalog/index.html')
    context = {
        'movie_list': movie_list,
        'num_movies': num_movies,
    }
    return HttpResponse(render(request, 'moviecatalog/index.html', context))


def detail(request, movie_id):
    movie = get_object_or_404(Movie, mk=movie_id)
    return render(request, 'moviecatalog/detail.html', {'movie': movie})