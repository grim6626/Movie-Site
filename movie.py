
import webbrowser

class Movie():

    def __init__(self, movie_title, movie_storyline, poster, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
