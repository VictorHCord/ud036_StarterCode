# My Favorite Movies Trailers
You can create a static page with all your favorite movie trailers.

#### Author
Tiago Mendes
<tetigo@gmail.com>

### Prerequisites
You must have python installed. 
Tested with python 2.7.9 and python3.6.6.

### How to create html file using my favorite movies list
- `git clone https://github.com/tetigo/ud036_StarterCode.git`
- `python entertainment_center.py`
- `a file called fresh_tomatoes.html will be created in the same folder`

### How to setup your favorite movies list
Open the file `media.py` for edit
Each movie must be an instance of Movie class containing:
- Title
- Description
- Poster Url (imdb)
- Trailer Url (Youtube)

Then we create a **list** of our previous movies.
Now just call `fresh_tomatoes.open_movies_page(your_films_list)`
This Module fresh_tomatoes was created and shared by **Udacity**.

### Example:
```
matrix = Movie(
    "Matrix",
    "A computer hacker learns from mysterious rebels about the true nature "
    "of his reality and his role in the war against its controllers.",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

warz = Movie(
    "World War Z",
    "Former United Nations employee Gerry Lane traverses the world in a "
    "race against time to stop the Zombie pandemic that is toppling armies "
    "and governments, and threatening to destroy humanity itself.",
    "https://upload.wikimedia.org/wikipedia/pt/f/fa/World_War_Z.jpg",
    "https://www.youtube.com/watch?v=Md6Dvxdr0AQ")

films_list = [matrix, warz]

fresh_tomatoes.open_movies_page(films_list)
```

### Thanks
Tiago



