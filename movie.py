from media import media
from ratingmixin import RatingMixin

class Movie(media, RatingMixin):
    def __init__(self, title, year, rating, genre, director):
        super().__init__(title, year, rating, genre)
        self.director = director

    def get_summary(self):
        return f"{self.title} ({self.year}) - {self.genre}, directed by {self.director}"
    
    def to_dict(self):
        return {
            'type': 'Movie',
            'title': self.title,
            'year': self.year,
            'rating': self.rating,
            'genre': self.genre,
            'director': self.director
        }
