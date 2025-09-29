from pydantic import BaseModel

class MediaBase(BaseModel):
    title: str
    year: int
    rating: float
    genre: str

class MovieCreate(MediaBase):
    director: str

class SeriesCreate(MediaBase):
    seasons: int

    
    