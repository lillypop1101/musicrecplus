"""
Nov. 25, 2024
Jem Riche, Naima Sana, Felicity Tabia
We pledge our honor that we have abided by the Stevens Honor System.
"""
data = {}
name = ""

with open("musicrecplus.txt", "w+") as file:
    name = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ")
    if name not in data:
        data[name] = []
        # enter preferences before showing menu

def print_menu():
    """ Gives the user a menu of options to input. """
    valid_options = ['e', 'r', 'p', 'h', 'm', 'q']
    while True:
        option = input("""
Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit
""")
        x = option.strip()
        if x in valid_options:
            return x
        else:
            print("Invalid option chosen. Please try again.")

def save_database(database, filename="musicrecplus.txt"):
    """ Saves the current database to the file. """
    with open(filename, 'w') as file:
        for user, artists in database.items():
            file.write(f"{user}:{','.join(artists)}\n")

def enter_preferences(database, user):
    """ Allows the user to input the artists they like. """
    artists = []
    while True:
        preference = input("Enter an artist you like (Enter to finish):").strip()
        if preference == "":
            break
        elif preference not in artists:
            artists.append(preference.title())
        database[user] = sorted(artists)
"""
def most_pop_artist(filename):
     Prints the artists that are liked by the most users.     
    artistscount = [] 
    with open(filename, 'r') as file:
        for user, artist in file:
            if artist not in artistscount:
                artist.append(artist: 1)
            if artist in artistscount:
"""



def menu_options():
    " Handles the user's choice from the menu. """
    while True:
        choice = print_menu()
        if choice == 'q':
            save_database(data)
            break
        elif choice == 'e':
            enter_preferences(data, name)
        elif choice == 'r':
            pass # Get recommendations
        elif choice == 'p':
            pass # Show most popular artists
        elif choice == 'h':
            pass # How popular is the most popular
        elif choice == 'm':
            pass # Which user has the most likes

menu_options()