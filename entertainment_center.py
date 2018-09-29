from media import Movie
import fresh_tomatoes
import requests
import json

omdb_key = 'xxxxxxxx'


def search_movie(title, omdb_key):
    try:
        # the api that we use to get the movie data
        req = requests.get('http://www.omdbapi.com/?t=' + title +
                           '&type=movie&apikey=' + omdb_key)

        # the api returns data in the type json (thats very good)
        # now we convert the data to dictionary to easily use inside
        # our program
        dic = json.loads(req.text)
        return dic
    except Exception as e:
        print('connection error', e)
        return None

# every time we want a new movie we call this funtion using
# the title and our key


movie = search_movie('blended', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

# we create an object of type movie
blended = Movie(
    0,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=8MuWt2X59fo")

movie = search_movie('matrix', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

matrix = Movie(
    1,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")


movie = search_movie('300', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

_300 = Movie(
    2,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=UrIbxk7idYA")

movie = search_movie('v for vendetta', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

vendetta = Movie(
    3,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=lSA7mAHolAw")

movie = search_movie('avatar', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

avatar = Movie(
    4,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movie = search_movie('the lord of the rings', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

lord = Movie(
    5,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=V75dMMIW2B4")

movie = search_movie('predator', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

predator = Movie(
    6,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=X2hBYGwKh3I")

movie = search_movie('the terminator', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

terminator = Movie(
    7,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=k64P4l2Wmeg")

movie = search_movie('alien 3', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

alien3 = Movie(
    8,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=KUTaNMJJBa8")

movie = search_movie('world war z', omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')

warz = Movie(
    9,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=Md6Dvxdr0AQ")

# we create a list of objects Movie
films_list = [blended, matrix, _300, vendetta, avatar, lord,
              predator, terminator, alien3, warz]

# black magic that creates a new page with our movies
fresh_tomatoes.open_movies_page(films_list)

# matrix.show_info()

# filme = search_movie('jurassic park',omdb_key)
# print('Titulo...: '+filme['Title'])
# print('Ano......: '+filme['Year'])
# print('Genero...: '+filme['Genre'])
# print('Duração..: '+filme['Runtime'])
# print('Sinopse..: '+filme['Plot'])
# print('Poster...: '+filme['Poster'])
# print('Website..: '+filme['Website'])
