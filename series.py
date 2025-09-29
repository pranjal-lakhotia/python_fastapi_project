from media import media
from ratingmixin import RatingMixin

class Series(media,RatingMixin):
    def __init__(self,title, year, rating, genre, seasons):
        super().__init__(title, year, rating, genre)
        self.seasons = seasons
     
    def get_summary(self):
         return f'{self.title} ({self.year}) - {self.genre}, {self.seasons} seasons'     
    
    def to_dict(self):
        return {
            'type': 'Series',
            'title': self.title,
            'year': self.year,
            'rating': self.rating,
            'genre': self.genre,
            'seasons':self.seasons
        }