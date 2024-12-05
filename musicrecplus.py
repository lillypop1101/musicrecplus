"""
Nov. 25, 2024
Jem Riche, Naima Sana, Felicity Tabia
We pledge our honor that we have abided by the Stevens Honor System.
"""

import os

class MusicRecPlus:
    def __init__(self, filename="musicrecplus.txt"):
        """Felicity: Initializes a new instance of the MusicRecPlus."""
        self.filename = filename
        self.data = self.read_file()
        self.user = None

    def read_file(self):
        """Naima: Reads the file and loads the data."""
        try:
            with open(self.filename, "r") as file:
                return {
                    user.strip(): [artist.strip() for artist in artists.split(",")]
                    for user, artists in (line.split(":") for line in file)
                }
        except FileNotFoundError:
            return {}

    def save_database(self):
        """Felicity: Saves the current database to the file."""
        with open(self.filename, "w") as file:
            for user, artists in self.data.items():
                file.write(f"{user}:{','.join(artists)}\n")

    def print_menu(self):
        """Felicity: Displays the menu and gets a valid user choice."""
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

    def enter_preferences(self):
        """Felicity: Allows the user to input the artists they like and replaces any existing preferences."""
        artists = set() 
        while True:
            preference = input("Enter an artist you like (Enter to finish): ").strip()
            if not preference:
                break
            artists.add(preference.title())  
        self.data[self.user] = sorted(artists)  

    def artist_likes(self):
        """Naima: Returns a dictionary of artist counts based on user preferences."""
        artists_count = {}
        for user, artists in self.data.items():
            if user.endswith("$"):
                continue
            for artist in artists:
                if artist == "":
                    continue
                if artist not in artists_count:
                    artists_count[artist] = 1
                else:
                    artists_count[artist] += 1
        return artists_count

    def most_pop_artist(self):
        """Naima: Prints the artists liked by the most users."""
        artists_count = self.artist_likes()
        if artists_count:
            result = 0
            while result < 3:
                top_artist = max(artists_count, key=lambda v: artists_count[v])
                print(top_artist)
                artists_count.pop(top_artist)
                result += 1
        else:
            print("Sorry, no artists found.")

    def how_pop_artist(self):
        """Naima: Prints the number of likes the most popular artist received."""
        artists_count = self.artist_likes()
        if artists_count:
            print(max(artists_count.values()))
        else:
            print("Sorry, no artists found.")

    def most_likes(self):
        """Naima: Prints the user(s) that like the most artists."""
        users_lst = []
        most = 0
        for user, artists in self.data.items():
            if user.endswith("$"):
                continue
            num_artists = len(artists)
            if num_artists >= most:
                if num_artists > most:
                    users_lst = []
                users_lst.append(user)
                most = num_artists
        if most == 0:
            print("Sorry, no user found")
        else:
            for userID in sorted(users_lst):
                print(userID)

    def get_rec(self):
        """Jem Riche: Prints recommended artists based on the most similar user preferences."""
        def similarity(user1, user2):
            """Helper function to find similarity"""
            sim = sum(1 for artist in user1 if artist in user2)
            return sim >= 2 and sim != len(user1) and sim != len(user2)

        similar = []
        rec_art = []

        for user in self.data:
            if user.endswith("$"):
                continue
            if similarity(self.data[self.user], self.data[user]):
                similar += self.data[user]

        for artist in similar:
            if artist not in self.data[self.user]:
                rec_art.append(artist)

        if rec_art:
            for artist in sorted(set(rec_art)):
                print(artist)
        else:
            print("No recommendations available at this time.")

    def menu_options(self):
        """Felicity: Handles the user's choice from the menu."""
        while True:
            choice = self.print_menu()
            if choice == 'q':
                self.save_database()
                break
            elif choice == 'e':
                self.enter_preferences()
            elif choice == 'r':
                self.get_rec()
            elif choice == 'p':
                self.most_pop_artist()
            elif choice == 'h':
                self.how_pop_artist()
            elif choice == 'm':
                self.most_likes()

    def run(self):
        """Jem Riche: Opens file, appends if file exists and writes if it does not."""
        if os.path.exists(self.filename):
            append_write = 'a+'
        else:
            append_write = 'w+'

        name = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")
        self.user = name.strip()
        if self.user not in self.data:
            self.data[self.user] = []
            self.enter_preferences()
        else:
            print(self.data[self.user])  # Show the existing preferences for testing

        self.menu_options()


if __name__ == "__main__":
    app = MusicRecPlus()
    app.run()