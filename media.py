import webbrowser


class Video():
    '''
    Armazana informacoes genericas sobre Videos
    This class provides a way to store Generic Video Info
    '''
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print('Title    : ' + self.title)
        print('Duration : ' + self.duration)


class Movie(Video):
    '''
    Essa classe serve para salvar informacoes basicas sobre filmes
    This class provides a way to store basic movies information
    '''

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, duration='n/a'):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_info(self):
        Video.show_info(self)
        print('Storyline: ' + self.storyline)
        print('Poster   : ' + self.poster_image_url)
        print('Trailer  : ' + self.trailer_youtube_url)


class TVShow(Video):
    '''
    Essa classe serve para salvar informacoes basicas sobre TV
    This class provides a way to store basic tv shows information
    '''

    def __init__(self, season, episode, tv_station,
                 title='n/a', duration='n/a'):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def show_info(self):
        Video.show_info(self)
        print('Season   : ' + self.season)
        print('Episode  : ' + self.episode)
        print('TVStation: ' + self.tv_station)


if __name__ == '__main__':

    Video('Generic Video', '120min').show_info()
    print('-' * 40)
    Movie('Generic Movie', 'Some Story',
          'poster url', 'youtube url').show_info()
    print('-' * 40)
    TVShow('Season 1', 'Episode 1', 'Fox', 'Walking Dead').show_info()
