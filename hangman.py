# Hangman Display
# Create visuals to write hangman as a user enters a wrong response
# hm = hangman

# Create the initial hangman base
class hmBase:
    def __init__(self):
        print('_____________')
        print('|            |')
        for i in range(7):
            print('             |')
game1 = hmBase()
game1

# Letters
# All 100 letters should be the same
# When letters are drawn it should occur randomly

# Players
# Each player should have a "rack" of available letters to play
# Once a letter is played, it should no longer be available to the player
# 
