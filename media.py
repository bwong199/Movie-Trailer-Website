import json
import fresh_tomatoes


# this is the movie class with a constructor that takes 1)title, 
# 2) post_image_url, and 3) youtube url trailer as inputs


class movie:
    def __init__(
            self,
            title,
            poster_image_url,
            trailer_youtube_url,
    ):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
