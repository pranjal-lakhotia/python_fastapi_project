from fastapi.testclient import TestClient
from api import app   # import your FastAPI app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Media Library API!"}

def test_add_movie():
    response = client.post(
        "/movies",
        json={"title": "Inception", "year": 2010, "rating": 9, "genre": "Sci-Fi", "director": "Nolan"}
    )
    assert response.status_code == 200
    assert "added successfully" in response.json()["message"]

def test_list_items():
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert "item" in data
    assert any("Inception" in s for s in data["item"])

def test_search_by_title():
    response = client.get("/search", params={"title": "Inception"})
    assert response.status_code == 200
    data = response.json()
    assert "Inception" in str(data)

def test_update_by_title():
    client.post('/movies',
                json={'title':'matrix','year':1999,'rating':8,'genre':'Thriller','director':'Wachowski'})
    response = client.patch('/items/matrix',
                            params={'rating':9, 'genre':'Action'})
    assert response.status_code == 200
    data = response.json()
    assert 'Action' in data['summary']
    
def test_delete_item():
    # add a movie first
    client.post(
        "/movies",
        json={"title": "Interstellar", "year": 2014, "rating": 9, "genre": "Sci-Fi", "director": "Nolan"}
    )

    # now delete it
    response = client.delete("/items/Interstellar")
    assert response.status_code == 200
    assert "deleted successfully" in response.json()["message"]

    # confirm it’s really gone
    check = client.get("/search", params={"title": "Interstellar"})
    assert "No item present" in check.json()["message"]


