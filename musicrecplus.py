"""
Nov. 25, 2024
Jem Riche, Naima Sana, Felicity Tabia
We pledge our honor that we have abided by the Stevens Honor System.
"""
data = {}
name = ""

with open("musicrecplus.txt", "a") as file:
    name = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ")
    if name not in data:
        data[name] = []
        # enter preferences before showing menu
    """else:
        for line in file:
            if name in line:"""

                
def print_menu():
    """ Felicity: Gives the user a menu of options to input. """
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
    """ Felicity: Saves the current database to the file. """
    with open(filename, 'w') as file:
        for user, artists in database.items():
            file.write(f"{user}:{','.join(artists)}\n")

def enter_preferences(database, user):
    """ Felicity: Allows the user to input the artists they like. """
    artists = []
    while True:
        preference = input("Enter an artist you like (Enter to finish):").strip()
        if preference == "":
            break
        elif preference not in artists:
            artists.append(preference.title())
        database[user] = sorted(artists)

def most_pop_artist(database):
    """Naima Sana - Prints the artists that are liked by the most users. """  
    artistscount = {} 
    result = 0
    for user, artists in database.items():
        if "$" in user:
            continue
        for artist in artists:
            if artist not in artistscount:
                artistscount[artist] = 1 
            else:
                artistscount[artist] += 1
    if bool(artistscount) == True:
        while result < 3:
            if bool(artistscount) == False:
                return ""
            print(max(artistscount))
            artistscount.pop(max(artistscount))
            result += 1
    else:
        print("Sorry, no artists found.")
    
def menu_options():
    " Felicity: Handles the user's choice from the menu. """
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
            most_pop_artist(data)
        elif choice == 'h':
            pass # How popular is the most popular
        elif choice == 'm':
            pass # Which user has the most likes

menu_options()