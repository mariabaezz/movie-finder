import requests

API_KEY = 'e44a40cb'
URL_BASE = 'http://www.omdbapi.com/'

def search_movie(title):
    params = {
        "apikey": API_KEY,
        "t": title
    }
    try:
        response = requests.get(URL_BASE, params=params)
    except requests.RequestException as e:
        print(f"Error fetching movie data: {e}")
        return None

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
    if results is None:
        print("Movie not found.")
    else:
        print(f"Title: {results['Title']}")
        print(f"Year: {results['Year']}")
        print(f"Genre: {results['Genre']}")
        print(f"Director: {results['Director']}")
        print(f"IMDb Rating: {results['IMDb_Rating']}\n")

def menu():
    while True:
        print("\nWelcome to movie search!\n")
        print("1. Search for a movie")
        print("2. Exit\n")
        choice = (input("Enter your choice: "))
        if choice not in ["1", "2"]:
            print("Invalid choice. Please try again.")
            continue
        if choice == "1":
            title = input("Enter movie title: ")
            result = search_movie(title)
            show_results(result)
        if choice == "2":
            break
        
    print("Goodbye!")


if __name__ == "__main__":
    menu()