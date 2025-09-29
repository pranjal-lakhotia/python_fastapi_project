from typing import List
from media import media
import json

class Library:
    def __init__(self):
        # holds all Media objects (Movies, Series, etc.)
        self.items: List[media] = []
        self.load_from_file()

    def add_item(self, item: media):
        """Add a media item (Movie, Series, etc.) to the library."""
        if not isinstance(item, media):
            raise TypeError('Item provided must be of type media')
        self.items.append(item)

    def list_items(self):
        """Return all items in the library."""
        if not self.items:
            return 'list is empty'
        summaries = []
        for item in self.items:
            summaries.append(f'{item.get_summary()} | Rating: {item.rating}')
        return summaries

    def search_by_title(self, title: str):
        """Find media items by title (case-insensitive)."""
        for item in self.items:
            if item.title.lower() == title.lower():  # case-insensitive search
                return item
        return None

    def filter_by_genre(self, genre: str):
        """Find all media items that match a genre."""
        if not self.items:
            return "Library is empty."
        
        results = [item.get_summary() for item in self.items if item.genre.lower() == genre.lower()]
        if not results:
            print(f'No result found for selected genre {genre}')
        return results

    def top_rated(self, n: int = 5):
        """Return the top N items sorted by rating."""
        if not self.items:
            return "Library is empty."
        
        sorted_items = sorted(self.items, key=lambda x: x.rating, reverse=True)
        top_items = sorted_items[:n]
        return [f'{item.get_summary()} | Rating: {item.rating}' for item in top_items]
    
    def save_to_file(self):
        data = [item.to_dict() for item in self.items]
        print(data)
        with open('library.json', 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_from_file(self, filename = 'library.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item_data in data:
                    if item_data['type'] == 'Movie':
                        from movie import Movie
                        movie = Movie(item_data['title'], 
                            item_data["year"],
                            item_data["rating"],
                            item_data["genre"],
                            item_data["director"]
                        )
                        self.items.append(movie)
                    elif item_data['type'] == 'Series':
                        from series import Series
                        series = Series(item_data['title'],
                                    item_data["year"],
                                    item_data["rating"],
                                    item_data["genre"],
                                    item_data['seasons'])
                        self.items.append(series)
                    
        except FileNotFoundError:
            self.items = []
        except json.JSONDecodeError:
            self.items = []
        
            
        
