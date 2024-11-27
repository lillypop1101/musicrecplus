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

def save():
    " When the user selects 'q', it saves and quits. """
    pass

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
    
