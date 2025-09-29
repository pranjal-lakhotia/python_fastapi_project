import pytest
from movie import Movie
from series import Series
from library import Library

def test_movie_creation():
    movie = Movie("Inception", 2010, 9, "Sci-Fi", "Nolan")
    assert movie.title == "Inception"
    assert movie.year == 2010
    assert movie.rating == 9
    assert movie.genre == "Sci-Fi"
    assert movie.director == "Nolan"
    assert "Inception" in movie.get_summary()   # check summary contains title

def test_series_creation():
    series = Series("Breaking Bad", 2008, 10, "Crime", 5)
    assert series.title == "Breaking Bad"
    assert series.seasons == 5
    assert "Breaking Bad" in series.get_summary()
    
def test_add_and_list_items():
    lib = Library()
    movie = Movie("Matrix", 1999, 9, "Sci-Fi", "Wachowski")
    lib.add_item(movie)

    assert len(lib.items) == 1
    assert lib.items[0].title == "Matrix"

def test_search_by_title_found():
    lib = Library()
    movie = Movie("Inception", 2010, 9, "Sci-Fi", "Nolan")
    lib.add_item(movie)

    results = lib.search_by_title("Inception")
    assert results != "No media found with title 'Inception'."  # not empty
    assert "Inception" in results[0]   # should contain title

def test_search_by_title_not_found():
    lib = Library()
    results = lib.search_by_title("Unknown")
    assert results == "No media found with title 'Unknown'."

def test_filter_by_genre():
    lib = Library()
    lib.add_item(Movie("Inception", 2010, 9, "Sci-Fi", "Nolan"))
    lib.add_item(Movie("Interstellar", 2014, 8, "Sci-Fi", "Nolan"))
    lib.add_item(Movie("Joker", 2019, 8, "Drama", "Todd Phillips"))

    sci_fi_movies = lib.filter_by_genre("Sci-Fi")
    assert len(sci_fi_movies) == 2
    assert all("Sci-Fi" in m for m in sci_fi_movies)

