import requests

API_KEY = 'e44a40cb'
URL_BASE = 'http://www.omdbapi.com/'

def search_movie(title):
    params = {
        "apikey": API_KEY,
        "t": title
    }
    response = requests.get(URL_BASE, params=params)
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

def menu():
    while True:
        print("Welcome to movie search!")
        print("1. Search for a movie")
        print("2. Exit")
        choice = int(input("Enter your choice: "))
        if choice > 2 or choice < 1:
            print("Invalid choice. Please try again.")
            return menu()
        if choice == 1:
            title = input("Enter movie title: ")
            result = search_movie(title)
            if result is None:
                print("Movie not found.")
            else:
                print(f"Title: {result['Title']}")
                print(f"Year: {result['Year']}")
                print(f"Genre: {result['Genre']}")
                print(f"Director: {result['Director']}")
                print(f"IMDb Rating: {result['IMDb_Rating']}")
            menu()
        if choice == 2:
            break
        
        print("Goodbye!")
        exit()

if __name__ == "__main__":
    menu()