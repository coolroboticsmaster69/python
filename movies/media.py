import webbrowser


class Movie():
    VALID_RATINGS = ["G","PG","PG-18","R"]
    def __init__ (self,movie_title,movie_storyline,poster_image,trailer_youtube,release_date,review_link):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.release_date=release_date
        self.review_link=review_link

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
