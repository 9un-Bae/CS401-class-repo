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
    """
    Desc: Finds the movie with the highest net profit
    Args: Data (List[Dict]): List of movie dictionaries
    Returns: Dict[str, Union[str, float]]: Dictionary with the movie title as the key and the highest net profit as the value
    """

    max_profit = float('-inf')  # Start with the smallest possible number
    max_profit_movie = "Unknown"

    for movie in data:
        try:
            # Ensure values exist and are valid numbers
            if not movie["grossWorldWide"] or not movie["budget"]:
                continue

            profit = movie["grossWorldWide"] - movie["budget"]
            if profit > max_profit:
                max_profit = profit
                max_profit_movie = movie['Title']

        except KeyError as e:
            logging.warning(f"Missing key in movie data: {e}")
        except TypeError:
            logging.warning("Invalid type")

    return {max_profit_movie : max_profit} 


# TODO: add second function to print out interesting statistics about the data
def most_common_genre(data):
    """
    Desc: Determines the most common genre among movies
    Args: Data (List[Dict]): List of movie dictionaries
    Returns: str: The most frequently occurring genre
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
    Args: Data (List[Dict]): List of movie dictionaries
    Returns: Tuple[List[str], float]: tuple containing a list of top directors and their best rating
    """

    best_rating = 0.0
    directors = []

    director_ratings = {}
    for movie in data:
        if movie['directors'] and movie['Rating']:
            if movie['Rating'] > best_rating:
                best_rating = movie['Rating']
                directors = movie['directors']
    
    return directors, best_rating

def main():

    if len(sys.argv) < 2:
        print("Error: No command line argument provided. Please provide a file name for a json file to read. i.e. python analyze_data.py data.json")
        sys.exit(1)    # Exit with a non-zero status code to indicate an error

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
    print(f'Top director by rating: {best_director}')

if __name__ == '__main__':
    main()