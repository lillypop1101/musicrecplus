"""
Nov. 25, 2024
Jem Riche, Naima Sana, Felicity Tabia
We pledge our honor that we have abided by the Stevens Honor System.
"""

import os.path
from pathlib import Path

path = os.path.abspath(os.getcwd()) + "\\musicrecplus.txt"
data = {}
name = ""


"""Jem Riche: Opens file, appends if file exists and writes if it does not."""
if os.path.exists(path):
    append_write = 'a+'
else:
    append_write = 'w+' 

file = open(path,append_write)
name = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ")
if name not in data:
    data[name] = []

def read_file():
    data = {}
    with open("musicrecplus.txt", "r") as file:
        for line in file:
            users, artists = line.strip().split(":")
            artists_list = [s.strip() for s in artists.split(",")]
            data[users.strip()] = artists_list
    return data
read_data = read_file()

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
    #with open(filename, 'w') as file:
    for user, artists in database.items():
        file.close()

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
    for user, artists in database.items():
        file.write(f"{user}:{','.join(artists)}\n")
        file.close()
    read_data = read_file()

def artist_likes(database):
    artistscount = {} 
    for user, artists in database.items():
        if user.endswith("$"):
            continue
        for artist in artists:
            if artist == "":
                continue
            if artist not in artistscount:
                artistscount[artist] = 1 
            else:
                artistscount[artist] += 1
    return artistscount

def most_pop_artist(database):
    """Naima Sana - Prints the artists that are liked by the most users. """  
    artistscount = artist_likes(database)
    result = 0
    if bool(artistscount) == True:
        while result < 3:
            if bool(artistscount) == False:
                return ""
            top_artist = max(artistscount, key = lambda v: artistscount[v])
            print(top_artist)
            artistscount.pop(top_artist)
            result += 1
    else:
        print("Sorry, no artists found.")

def how_pop_artist(database):
    """Naima Sana - Print the number of likes the most popular artist received.""" 
    artistscount = artist_likes(database)
    if bool(artistscount) == True:
        print(max(artistscount.values()))
    else:
        print("Sorry, no artists found.")

def most_likes(database):
    """Jem Riche - Prints the user(s) that like the most artists. """
    users_lst = []
    most = 0
    
    for user, artists in database.items():
        if user.endswith("$"):
            continue
        
        numArtists = len(database[user])
        if numArtists >= most:
            if numArtists > most:
                users_lst = []
                
            users_lst.append(user)
            most = numArtists

    if most == 0:
        print("Sorry, no user found")
        
    else:
        for userID in sorted(users_lst):
            print(userID)

def get_rec(database):
    """Jem Riche - Prints recommended artists based off of users with the most similar preferences. """

    similar = []
    recArt = []
    
    def similarity(user1, user2):
        """Helper function to find similarity"""
        sim = 0
        for artist in user1:
            if artist in user2:
                sim += 1

        if sim>=2:
            if sim != len(user1) and sim != len(user2):   # makes sure they are not identical
                return True
        return False

    """Getting the recommendations"""
    for user in database:
        if user.endswith("$"):
            continue
        if similarity(database[name], database[user]) == True:
            similar += database[user]
            
    for i in similar:
        if i not in database[name]:
            recArt.append(i)
    

    if len(recArt) > 0:
        for artist in sorted(list(set(recArt))):
            print(artist)
    else:
        print("No recommendations available at this time.")


    
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
            get_rec(read_data)
        elif choice == 'p':
            most_pop_artist(read_data)
        elif choice == 'h':
            how_pop_artist(read_data)
        elif choice == 'm':
            most_likes(read_data)

menu_options()
