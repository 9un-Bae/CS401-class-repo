from analyze_data import net_profit
import pytest

def test_net_profit():
    # TODO: write unit tests for net profit function 
    """
    Test net_profit function with sample movie data.
    """
    sample_data1 = [
        {"title": "Movie A", "grossWorldwide": 500000, "budget": 200000},
        {"title": "Movie B", "grossWorldwide": 1000000, "budget": 300000},
        {"title": "Movie C", "grossWorldwide": 750000, "budget": 250000}
    ]
    sample_data2 = [
        {"title": "Movie X", "grossWorldwide": 2000000, "budget": 500000},
        {"title": "Movie Y", "grossWorldwide": 1500000, "budget": 600000}
    ]
    sample_data3 = []
    
    assert net_profit(sample_data1) == "Movie B"
    assert net_profit(sample_data2) == "Movie X"
    assert net_profit(sample_data3) == ""


# TODO: write unit tests for second function in analyze_data.py
def test_most_common_genre():
    """
    Test most_common_genre function with sample movie data.
    """
    sample_data1 = [
        {"genres": ["Action", "Comedy"]},
        {"genres": ["Action", "Drama"]},
        {"genres": ["Action"]}
    ]
    sample_data2 = [
        {"genres": ["Drama", "Horror"]},
        {"genres": ["Drama", "Thriller"]},
        {"genres": ["Drama"]}
    ]
    sample_data3 = []
    
    assert most_common_genre(sample_data1) == "Action"
    assert most_common_genre(sample_data2) == "Drama"
    assert most_common_genre(sample_data3) == "Unknown"

# TODO: write unit tests for second function in analyze_data.py
def test_top_director_by_rating():
    """
    Test top_director_by_rating function with sample movie data.
    """
    sample_data1 = [
        {"director": "Director A", "rating": 8.5},
        {"director": "Director B", "rating": 7.0},
        {"director": "Director A", "rating": 9.0}
    ]
    sample_data2 = [
        {"director": "Director X", "rating": 6.0},
        {"director": "Director Y", "rating": 9.5},
        {"director": "Director X", "rating": 7.5}
    ]
    sample_data3 = []
    
    assert top_director_by_rating(sample_data1) == "Director A"
    assert top_director_by_rating(sample_data2) == "Director Y"
    assert top_director_by_rating(sample_data3) == "Unknown"