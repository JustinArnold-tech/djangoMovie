from django.shortcuts import render
from django.http import HttpResponse
import requests

APIKEY = 'e9ee25ea'
POSTER_KEY = 'k_36k6exf5'
# def movie(request):
#     movie_ = request.POST['movie']
#     return movie_




def index(request):

    if request.method == 'POST':

        data_URL = f'http://www.omdbapi.com/?apikey={APIKEY}'
        year = ''
        # movie = movie()
        params = {
            't':request.response,
            'type':'movie',
            'y':year,
            'plot':'full'
        }

        try:
            response = requests.get(data_URL,params=params).json()
        except Exception as e:
            raise e
        

        Title = response['Title']
        released = response['Released']
        Rating = response['Rated']
        Runtime = response['Runtime']
        Genre = response['Genre']
        Director = response['Director']
        Writer = response['Writer']
        Actors = response['Actors']
        Plot = response['Plot']
        Id = response['imdbID']
        
        info = { 
            'Title' : Title,
            'released' : released,
            'Rating' : Rating,
            'Runtime' : Runtime, 
            'Genre' : Genre,
            'Director' : Director,
            'Writer' : Writer,
            'Actors' : Actors,
            'Plot' : Plot,
        }
        try:
            poster_info = requests.get(f'https://imdb-api.com/en/API/Posters/{POSTER_KEY}/{Id}').json()
        except Exception as e:
            raise e

        
        poster = poster_info['posters'][0]['link']
        return render('movie_info/movie.html', poster=poster, **info)



    return render(request, 'movie_info/index.html')
# Create your views here.