import webbrowser


class Movie():
    """
    A class that contains the information and functions of the motion object to
    retrieve as information
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ Inits Movie with movie title, storyline, poster image, and trailer
            Args:
                movie_title: The movies title
                storyline: Movies story line
                poster_image: A url of the poster image
                trailer_youtube: A url of the trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open the browser to play the movie trailer"""
        webbrowser.open(self.trailer_youtube_url)

    def show_info(self):
        """Print the movie title and storyline"""
        print(self.title)
        print(self.storyline)
