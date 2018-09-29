import webbrowser
import os


# Styles and scripting for the page
main_page_head = '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Favorite Movie Trailers</title>

        <!-- Styles -->
        <link href="css/lightbox_alt.css" rel="stylesheet" />
        <link href="css/lightbox.css" rel="stylesheet" />
        <link rel="stylesheet" href="css/bootstrap.min.css">

        <!-- Scripts -->
        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script src="js/lightboxController.js"></script>
        <script src="js/index.js"></script>

        <!-- Webfonts -->
        <link href="css/montserrat.css" rel="stylesheet">
    </head>
'''


# The main page layout and title bar
main_page_content = '''
    <body>

        <header class="gblHead">
            <h1>My Favorite Movie Trailers v1.2</h1>
            <a class="tigo" href="mailto:tetigo@gmail.com">Tiago Mendes</a>
        </header>

        <div class="container contentWrap">
            <div class="row">
                {movie_tiles}
            </div>
        </div>

    </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
            <article class="col-12 col-md-3 col-sm-6 col-lg-2 blox bloxPopup"\
             data-src="{trailer_youtube_url}" data-id="{id}">
                <div class="featured">
                    <img src="{poster_image_url}" alt="" >
                </div>
                <div class="content">
                    <p>{movie_title}</p>
                </div>
            </article>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            id=movie.ident,
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_url=movie.trailer_youtube_url
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
