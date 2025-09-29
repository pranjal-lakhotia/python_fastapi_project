from movie import Movie
from series import Series
from library import Library

lib = Library()
lib.add_item(Movie("Inception", 2010, 8.8, "Sci-Fi", "Christopher Nolan"))
lib.add_item(Series("Breaking Bad", 2008, 9.5, "Crime", 5))
lib.add_item(Movie("Interstellar", 2014, 8.6, "Sci-Fi", "Christopher Nolan"))

print(lib.filter_by_genre("Sci-Fi"))
print("Top rated:\n", lib.top_rated(2))
