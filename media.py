# import necessarry modules
import webbrowser
# this class is used to create movie objects


class Movie():
    """ THis class provides a way to store movie related information:
    a title, poster image url and a trailer video url."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
        self, movie_title, movie_storyline,
        poster_image, trailer_youtube
                ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# a method opens a browser page with video trailer of a movie using a link
#    def show_trailer(self):
#        webbrowser.open(self.trailer_youtube_url)
