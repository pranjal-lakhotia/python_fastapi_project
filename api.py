from fastapi import FastAPI
from library import Library
from movie import Movie
from series import Series
from mediabase import MovieCreate
from mediabase import SeriesCreate
from fastapi import HTTPException
from media import media
from contextlib import asynccontextmanager


library = Library()

@asynccontextmanager
async def lifespan(app: FastAPI):
    library.load_from_file()
    yield
    library.save_to_file()

app = FastAPI(lifespan=lifespan)
@app.get('/')
def root():
    return {"message": "Welcome to the Media Library API!"}

@app.get('/items')
def list_items():
    if not library.items:
        return {'message': 'list is empty'}
    return {'item': [item.get_summary() for item in library.items]}

@app.post('/movies')
def add_movie(movie: MovieCreate):
    new_movie = Movie(movie.title,movie.year,movie.rating,movie.genre,movie.director)
    library.add_item(new_movie)
    return {'message': f'Movie {movie.title} added successfully !!'}

@app.post('/series')
def add_series(new_series:SeriesCreate):
    series = Series(new_series.title, new_series.year, new_series.rating, new_series.genre, new_series.seasons)
    library.add_item(series)
    return {"message": f"Series '{new_series.title}' added successfully!"}

@app.get('/search')
def get_item_by_title(title: str):
    item = library.search_by_title(title)
    if not item:
        return {'message':f'No item present with given title: {title}'}
    return {'item': item.get_summary()}

@app.get('/genre')
def get_item_by_genre(genre: str):
    results = library.filter_by_genre(genre)
    if not results:
        return {'message':f'No item present with given genre: {genre}'}
    return {'item': results}

@app.get("/top_rated")
def top_rated(n: int = 5):
    results = library.top_rated(n)
    return {"top_rated": results}

@app.patch('/items/{title}')
def update_item(title: str, rating: float = None, genre: str = None):
    item = library.search_by_title(title)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    if rating is not None:
        if 0 <= rating <= 10: 
            item.rating = rating
        else:
            raise HTTPException(status_code=400,detail='Rating should be between 0 - 10')
    if genre is not None:
        item.genre = genre
    return {'message': f'{title} updated !!', 'summary': item.get_summary()}

@app.delete('/items/{title}')
def remove_item(title:str):
    item = library.search_by_title(title)
    if not item:
        raise HTTPException(status_code=404,detail='Item not found')
    library.items.remove(item)
    return {'message': f'{title} deleted successfully !!'}

