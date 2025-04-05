import json
import logging

from flask import Flask, request, jsonify
from typing import List, Dict

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Helper function to retrieve data from the movies.json file
def get_data() -> list[dict]:
    """
    Retrieve the movies dataset and return it as a list of dictionaries
    Returns - List[Dict]: containing the movies dataset
    """
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading movies.json: {e}")
        return []  # Return an empty list if an error occurs

# TODO: Add a route to return the entire dataset
@app.route('/movies')
def movie():
    """
    Return the entire movies dataset
    Returns - List[Dict]: of all movies
    """
    logging.debug("Fetching entire movie dataset.")

    data = get_data()
    return jsonify(data)


# TODO: Add a route, or modify an existing route, to return the movies that are between a certain release year range
@app.route('/movies/range')
def movie_range():
    """
    Return movies within a specific release year range
    Returns: Dict: movies in the specified range or an error message
    """
    logging.debug("Fetching movies within a given year range.")

    start = request.args.get('start', type=int, default=0)
    end = request.args.get('end', type=int, default=0)

    data = get_data()

    if start is None or end is None:
        return jsonify({"error": "Invalid year range provided."}), 400

    result = [movie for movie in data if movie['Year'] and start <= movie['Year'] <= end]

    return jsonify(result) if result else jsonify({"error": "No movies found in the specified range."}), 200


# TODO: Add a route to return a movie if it matches the id
@app.route('/movies/<int:movie_id>', methods=['GET'])
def movie_id(movie_id: int):
    """
    Return a movie matching the provided movie ID
    Returns - Dict: movie ID or an error message
    """
    logging.debug("Fetching movie by ID.")
    
    data = get_data()

    for movie in data:
        if movie['id'] == movie_id:
            return jsonify(movie)

    return jsonify({"error": f"Movie with ID {movie_id} not found"}), 404


# TODO: Add a route to return the genres for a specific movie
@app.route('/movies/<int:movie_id>/genres')
def movie_genres(movie_id: int):
    """
    Return the genres of a specific movie by movie ID
    Returns - Dict: movie genres or an error message
    """
    logging.debug(f"Fetching genres for movie ID {movie_id}.")
    
    data = get_data()

    for movie in data:
        if movie["id"] == movie_id:
            return jsonify({"Title": movie["Title"], "genres": movie["genres"]})

    return jsonify({"error": f"Movie with ID {movie_id} not found"}), 404

# TODO: Add a route to return a movie if it matches the title
@app.route('/movies/mpa')
def movie_mpa():
    """
    Return a movie that matches the provided rating
    Returns - List[Dict]: A list of movies with the specified rating
    """
    logging.debug("Fetching movies by MPA rating.")
    
    movie_mpa = request.args.get('movie_mpa', type=str)

    data = get_data()
    
    results = [movie for movie in data if movie["MPA"] == movie_mpa]
    return jsonify(results) if results else jsonify({"error": f"No movies found with MPA rating '{movie_mpa}'"}), 200

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')