# My Favorite Movies Trailers v1.1
You can create a static page with all your favorite movie trailers.
In this version the page was recreated using bootstrap 3 for responsiveness.
Also using some jQuery and Lightbox for modal video.
All images was located on the internet, then resized to (259x383) using 
the site: http://resizeimage.net/ with image quality using 48%.
Then the resulting image was uploaded to https://pt-br.imgbb.com/.
This is the image used here inside my list.

#### Author
Tiago Mendes
<tetigo@gmail.com>

#### Prerequisites
You must have python installed. 
Tested with python 2.7.9 and python3.6.6.

#### Notes
This is a beta version yet. It's not finished and has a lot of work to
do yet. If you can help me, let me know. 
For example, I need help with a javascript function to close the modal 
video. Since the javascript code is not mine and I don't code it enought
yet, I don't know how to do it. And I'd love to have this function 
included in the project.

#### How to create html file using my favorite movies list
- `git clone https://github.com/tetigo/ud036_StarterCode.git`
- `python entertainment_center.py`
- `a file called fresh_tomatoes.html will be created in the same folder`

#### How to setup your favorite movies list
Open the file `media.py` for edit
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
matrix = Movie(
    1,
    "Matrix",
    "A computer hacker learns from mysterious rebels about the true nature "
    "of his reality and his role in the war against its controllers.",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

warz = Movie(
    2,
    "World War Z",
    "Former United Nations employee Gerry Lane traverses the world in a "
    "race against time to stop the Zombie pandemic that is toppling armies "
    "and governments, and threatening to destroy humanity itself.",
    "https://upload.wikimedia.org/wikipedia/pt/f/fa/World_War_Z.jpg",
    "https://www.youtube.com/watch?v=Md6Dvxdr0AQ")

films_list = [matrix, warz]

fresh_tomatoes.open_movies_page(films_list)
```

#### Thanks
[Tiago](mailto://tetigo@gmail.com)

