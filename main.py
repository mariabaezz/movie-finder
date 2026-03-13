import requests
import json

API_KEY = 'e44a40cb'
URL_BASE = 'http://www.omdbapi.com/'

def search_movie(title):
    params = {
        "apikey": API_KEY,
        "t": title
    }
    try:
        response = requests.get(URL_BASE, params=params, timeout=5)
    except requests.RequestException as e:
        print(f"Error fetching movie data")
        
        return "error"

    response = response.json()
    if response['Response'] == 'False':
        return None
    else:
        return {
            "Title": response['Title'],
            "Year": response['Year'],
            "Genre": response['Genre'],
            "Director": response['Director'],
            "IMDb_Rating": response['imdbRating']
        }
def show_results(results):
    if results == "error":
        print("An error occurred while fetching the movie data. Please try again.")
    elif results is None:
        print("Movie not found. Please check the title and try again.")
    else:
        print(f"Title: {results['Title']}")
        print(f"Year: {results['Year']}")
        print(f"Genre: {results['Genre']}")
        print(f"Director: {results['Director']}")
        print(f"IMDb Rating: {results['IMDb_Rating']}\n")

def save_rating(movie,rating):
    rating_data = {'title': movie['Title'], 'year': movie['Year'], 'rating': rating}
    try:
        with open ("movie_rating.json", "r") as f:
            ratings = json.load(f)
    except FileNotFoundError:
        ratings = []
    for r in ratings:
        if r['title'] == movie['Title'] and r['year'] == movie['Year']:
            print("You have already rated this movie. Updating your rating.")
            r['rating'] = rating
            break
    else:
        ratings.append(rating_data)
    with open("movie_rating.json", "w") as f:
        json.dump(ratings, f, indent=4)

def show_ratings():
    try:
        with open("movie_rating.json", "r") as f:
            ratings = json.load(f)
            for rating in ratings:
                print(f"Title: {rating['title']}, Rating: {rating['rating']}")
            average_rating = sum(float(r['rating']) for r in ratings) / len(ratings)
            print(f"You have rated {len(ratings)} movies with an average of :{average_rating}")
    except FileNotFoundError:
        print("No ratings found.")

def compare_ratings(movie):
    try:
        with open("movie_rating.json", "r") as f:
            ratings = json.load(f)
            for rating in ratings:
                if rating['title'] == movie['Title'] and rating['year'] == movie['Year']:
                    print(f"Your rating: {rating['rating']}")
                    print(f"IMDb rating: {movie['IMDb_Rating']}")
                    break
            else:
                print("You have not rated this movie yet.")
    except FileNotFoundError:
        print("No ratings found.")

def menu():
    while True:
        print("\nWelcome to movie search!\n")
        print("1. Search for a movie")
        print("2. Show my ratings")
        print("3. Compare my rating with IMDb rating")
        print("4. Exit\n")
        choice = (input("Enter your choice: "))
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue
        if choice == "1":
            title = input("Enter movie title: ")
            result = search_movie(title)
            show_results(result)
            if result is not None and result != "error":
                rate_movie = input("Would you like to rate this movie? (yes/no): ")
                if rate_movie == "yes":
                    rating = (input("Enter your rating (0-10): "))
                    if rating.isdigit() and 0 <= int(rating) <= 10:
                        save_rating(result, rating)
                    else:
                        print("Invalid rating. Please enter a number between 0 and 10.")
        if choice == "2":
            show_ratings()
        if choice == "3":
            title = input("Enter movie title to compare ratings: ")
            result = search_movie(title)
            if result is not None:
                compare_ratings(result)
            else:
                print("Movie not found. Please check the title and try again.")
        if choice == "4":
            break
        
    print("Goodbye!")


if __name__ == "__main__":
    menu()