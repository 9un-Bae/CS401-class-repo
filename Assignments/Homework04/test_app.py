import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# TODO: write a test for the entire dataset route
def test_movie(client):
    response = client.get('/movies')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0  # Ensure dataset is not empty

    for movie in data:
        assert isinstance(movie, dict)
        assert "Title" in movie
        assert "Year" in movie
        assert "genres" in movie
        assert "directors" in movie
        assert "Rating" in movie

# TODO: write a test for the movies between a certain release year range route
def test_movie_range(client):
    response = client.get('/movies/range?start=2020&end=2021')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0  # Ensure dataset is not empty

    for movie in data:
        year = int(movie.get("Year", 0))
        assert 2020 <= year <= 2021  # Check that year is within the specified range

# TODO: write a test for the movie by id route
def test_movie_id(client):
    response = client.get('/movies/1')  # Assuming movie with ID 1 exists
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert "Title" in data
    assert "Year" in data
    assert "genres" in data
    assert "directors" in data
    assert "Rating" in data

    # Test for a non-existent movie ID
    response = client.get('/movies/99999')  # Assuming this ID does not exist
    assert response.status_code == 404

# TODO: write a test for the genres by movie route
def test_movie_genres(client):
    response = client.get('/movies/1/genres')  # Assuming movie with ID 1 exists
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert len(data) > 0  # Ensure genres list is not empty

    for genre in data:
        assert isinstance(genre, str)  # Check that each genre is a string

    # Test for a non-existent movie ID
    response = client.get('/movies/99999/genres')  # Assuming this ID does not exist
    assert response.status_code == 404

# TODO: write a test for the movie by title route
def test_movie_mpa(client):
    response = client.get('/movies/mpa?movie_mpa=PG-13')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0  # Ensure dataset is not empty
    
    for movie in data:
        assert isinstance(movie, dict)
        assert "Title" in movie
        assert "Year" in movie
        assert "genres" in movie
        assert "directors" in movie
        assert "Rating" in movie
        # Check that the movie's MPA rating is PG-13
        assert movie["MPA"] == "PG-13"