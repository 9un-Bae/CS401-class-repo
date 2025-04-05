# 🎥 Flask Movie API 🍿

## 📖 Description
This project provides a Flask-based RESTful API to interact with a movies dataset stored in `movies.json`.  
Users can fetch all movies, search by year range, get details by ID, explore genres, and filter by MPA rating.  
The app is containerized using Docker and tested using `pytest` for reliability.

---

## 📂 Contents
1. **app.py** - Main Flask API application
2. **test_app.py** - Unit tests to verify functionality of the API
3. **movies.json** - Movie dataset used by the API
4. **Dockerfile** - Configuration file for Docker containerization

---

## 📦 Building the Docker Image
To build the Docker image, run:
```sh
docker build -t flask-movie-app .
```

---

## 🧪 Running Tests
Before or after starting the server, you can run unit tests:
```sh
pytest
```

---

## 🏃🏻‍♂️ Running the App Locally (with Flask)
To run the API directly using Flask on port `5001`:
```sh
flask --app app --debug run -p 5001
```

---

## 🐳 Running the App in Docker
To run the API from the Docker container (binding host port `5001` to container port `5000`):
```sh
docker run -p 5001:5000 flask-movie-app
```

You can now visit your API at:  
[localhost:5001/movies](localhost:5001/movies)

---

## 🔁 Available Endpoints

| Method | Route                        | Description                                 |
|--------|------------------------------|---------------------------------------------|
| GET    | `/movies`                   | Returns all movies                          |
| GET    | `/movies/range?start=YYYY&end=YYYY` | Filters movies by release year range |
| GET    | `/movies-id?movie_id=ID`    | Returns a movie by its ID                   |
| GET    | `/movies/<int:movie_id>/genres` | Returns genres for a specific movie     |
| GET    | `/movies/title?movie_mpa=RATING` | Filters movies by MPA rating            |