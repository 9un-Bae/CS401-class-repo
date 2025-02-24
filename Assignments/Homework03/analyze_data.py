import sys
import json
import logging

logging.basicConfig(level=logging.DEBUG)

def read_json(file_path: str):
    # TODO: read the JSON file and return the data
    """
    Desc: Reads a JSON file and returns the data
    Args: File_path (str): The path to the JSON file
    Returns: Dictionary containing movie data
    """

    logging.debug(f'Reading JSON file: {file_path}')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)

def net_profit(data):
    # TODO: movie with the largest net profit of the past 5 years
    """
    Desc: Finds the movie with the highest net profit
    Args: Data (list): List of movie dictionaries
    Returns: The title of the movie with the highest net profit
    """

    max_profit = float('-inf')  # Start with the smallest possible number
    max_profit_movie = "Unknown"

    for movie in data:
        try:
            gross = movie.get('grossWorldwide', 0)
            budget = movie.get('budget', 0)

            # Ensure gross and budget are converted to integers, handling floats and strings
            gross = int(float(str(gross).replace(',', '')))
            budget = int(float(str(budget).replace(',', '')))

            # Skip movies with missing or invalid data
            if gross == 0 or budget == 0:
                print(f"Skipping movie {movie.get('title', 'Unknown')} due to missing or zero values. Gross: {gross}, Budget: {budget}")
                continue

            profit = gross - budget
            if profit > max_profit:
                max_profit = profit
                max_profit_movie = movie.get('title', 'Unknown')

        except ValueError:
            print(f"Skipping movie {movie.get('title', 'Unknown')} due to invalid number format. Gross: {gross}, Budget: {budget}")

    return max_profit_movie

# TODO: add second function to print out interesting statistics about the data
def most_common_genre(data):
    """
    Desc: Determines the most common genre among movies
    Args: Data (list): List of movie dictionaries
    Returns: The most frequently occurring genre
    """

    genres = []
    for movie in data:
        genres.extend(movie.get('genres', []))
    genre_count = {}
    for genre in genres:
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    most_common = max(genre_count, key=genre_count.get, default="Unknown")
    return most_common

# TODO: add third function to print out interesting statistics about the data
def top_director_by_rating(data):
    """
    Desc: Finds the director with the highest average movie rating
    Args: Data (list): List of movie dictionaries
    Returns: The director with the highest average rating
    """

    director_ratings = {}
    for movie in data:
        if 'director' in movie and 'rating' in movie:
            if movie['director'] in director_ratings:
                director_ratings[movie['director']].append(movie['rating'])
            else:
                director_ratings[movie['director']] = [movie['rating']]
    avg_ratings = {director: sum(ratings) / len(ratings) for director, ratings in director_ratings.items()}
    best_director = max(avg_ratings, key=avg_ratings.get, default="Unknown")
    return best_director

def main():

    if len(sys.argv) < 2:
        print("Error: No command line argument provided. Please provide a file name for a json file to read. i.e. python analyze_data.py data.json")
        sys.exit(1)  # Exit with a non-zero status code to indicate an error

    # Access the command line argument
    output_file = sys.argv[1]

    # TODO: call function to read JSON file and return data
    data = read_json(output_file)

    # TODO: call function to get the movie with the largest net profit of the past 5 years
    net_profit_answer = net_profit(data)
    print(f'Movie with largest net profit: {net_profit_answer}')

    # TODO: second function to return and print out 
    common_genre = most_common_genre(data)
    print(f'Most common genre: {common_genre}')

    # TODO: third function to return and print out result
    best_director = top_director_by_rating(data)
    print(f'Top director by average rating: {best_director}')

if __name__ == '__main__':
    main()