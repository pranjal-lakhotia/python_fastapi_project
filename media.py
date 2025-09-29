from abc import ABC, abstractmethod

class media(ABC):
    def __init__(self,title,year,rating,genre):
        self.title = title
        self.year = year
        self.rating = rating
        self.genre = genre

    @abstractmethod
    def get_summary(self):
        pass
    
    def is_classic(self,year):
        return True if self.year < 2000 else False
    
    def __repr__(self):
        return f'<Media: {self.title}  ({self.year}) - {self.rating}>'
        