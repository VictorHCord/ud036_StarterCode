# My Favorite Movies Trailers v1.2
You can create a static page with all your favorite movie trailers.
In this version the page was recreated using bootstrap 3 for responsiveness.
Also using some jQuery and Lightbox for modal video.
Now all info are get using API from http://www.omdbapi.com/ 

#### Author
Tiago Mendes
<tetigo@gmail.com>

#### Prerequisites
- You must have python installed. 
- Tested with python 2.7.9 and python3.6.6.
- To use with python 2.7.9 you need first install requests 
using this: `pip install requests`
- If you are going to use the obdbapi you must enter the site 
http://www.omdbapi.com/ then click the api_key button then enter
your email and you will get your API_KEY. Don't share it.

#### Notes
This is a beta version yet. It's not finished and has a lot of work to
do yet. If you can help me, let me know. 
For example, I need help with a javascript function to close the modal 
video. Since the javascript code is not mine and I don't code it enought
yet, I don't know how to do it. And I'd love to have this function 
included in the project.
Now that I'm using API, we get a lot more information about a movie.
You can edit the class Movie inside media.py to include all the info
that you want. Very cool.

#### How to create html file using my favorite movies list
- `git clone https://github.com/tetigo/ud036_StarterCode.git`
- `python entertainment_center.py`
- `a file called fresh_tomatoes.html will be created in the same folder`

#### How to setup your favorite movies list
Open the file `media.py` for edit

Setup the variable omdb_key = 'xxxxxxxx' with your key that you got 
from the site http://www.omdbapi.com

Each movie must be an instance of Movie class containing:
- ID Number (sequential number used for display video)
- Title
- Description
- Poster Url (imdb)
- Trailer Url (Youtube)

Then we create a **list** of our previous movies.
Now just call `fresh_tomatoes.open_movies_page(your_films_list)`
The original module fresh_tomatoes was created and shared by **Udacity**.
This version is an alternative using bootstrap

#### Example:
```
movie = search_movie('matrix',omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')
matrix = Movie(
    1,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

movie = search_movie('world war z',omdb_key)
if(movie['Response'] == 'False'):
    exit('Movie not found')
warz = Movie(
    9,
    movie['Title'],
    movie['Plot'],
    movie['Poster'],
    "https://www.youtube.com/watch?v=Md6Dvxdr0AQ")

films_list = [matrix, warz]

fresh_tomatoes.open_movies_page(films_list)
```

#### Thanks
[Tiago](mailto://tetigo@gmail.com)

