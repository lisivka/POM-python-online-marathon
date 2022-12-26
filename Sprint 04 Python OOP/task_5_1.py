"""
The basic premise of the game Gallows is to follow two rules:
-First character of next word must match last character of previous word.
-The word must not have already been said.

Below is an example of a Gallows game:
['word', 'dowry', 'yodel', 'leader', 'righteous', 'serpent']  #valid!
['motive', 'beach']  # invalid! - beach should start with "e"
['hive', 'eh', 'hive']  # invalid! - "hive" has already been said
Write a Gallows class that has two instance variables:
-words: a list of words already said.
-game_over: a boolean that is true if the game is over.

and two instance methods:
-play: a method that takes in a word as an argument and checks if it is valid
(the word should follow rules #1 and #2 above).
If it is valid, it adds the word to the words list, and returns the words list.
If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.
-restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false.
It should return "game restarted".

Examples:
my_gallows = Gallows()
my_gallows.play('apple') ➞ ['apple']
my_gallows.play('ear') ➞ ['apple', 'ear']
my_gallows.play('rhino') ➞ ['apple', 'ear', 'rhino']
my_gallows.words ➞ ['apple', 'ear', 'rhino']
# Words should be accessible.
my_gallows.restart() ➞ "game restarted"
# Words list should be set back to empty.
my_gallows.play('hostess') ➞ ['hostess']
my_gallows.play('stash') ➞ ['hostess', 'stash']
my_gallows.play('hostess') ➞ "game over"
# Words cannot have already been said.
my_gallows.play('apple') ➞ ['apple']
my_gallows.play('ear') ➞ ['apple', 'ear']
my_gallows.play('rhino') ➞ ['apple', 'ear', 'rhino']
# Corn does not start with an "o".
my_gallows.play('corn') ➞"game over"
my_gallows.words ➞ ['apple', 'ear', 'rhino']
my_gallows.restart() ➞ "game restarted"
my_gallows.words ➞ []
Answer:(penalty regime: 0
"""


class Gallows:

    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word_next):
        rule_1 = True if (not self.words) or word_next[0] == self.words[-1][-1] else False
        rule_2 = True if word_next not in self.words else False

        if rule_1 and rule_2:
            self.words.append(word_next)
            return self.words
        else:
            self.game_over = True
            return "game over"

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"


my_gallows = Gallows()
print(my_gallows.game_over)
print(my_gallows.play('apple'))
print(my_gallows.words)
print(my_gallows.play('ear'))
print(my_gallows.play('rhino'))
print(my_gallows.play('ocelot'))
print(my_gallows.game_over)
print(my_gallows.play('oops'))
print(my_gallows.game_over)
print(my_gallows.words)
# False
# ['apple']
# ['apple']
# ['apple', 'ear']
# ['apple', 'ear', 'rhino']
# ['apple', 'ear', 'rhino', 'ocelot']
# False
# game over
# True
# ['apple', 'ear', 'rhino', 'ocelot']
# print("=============================")
# my_gallows = Gallows()
# print(my_gallows.restart())
# print(my_gallows.words)
# print(my_gallows.game_over)
# print(my_gallows.play('hostess'))
# print(my_gallows.game_over, False)
# print(my_gallows.play('stash'))
# print(my_gallows.play('hostess'))
# print(my_gallows.words)
# # game restarted
# # []
# # False
# # ['hostess']
# # False False
# # ['hostess', 'stash']
# # game over
# # ['hostess', 'stash']

# print("=============================")

# my_gallows = Gallows()
# print(my_gallows.game_over)
# print(my_gallows.play('apple'))
# print(my_gallows.words)
# print(my_gallows.play('ear'))
# print(my_gallows.play('over'))
# print(my_gallows.game_over)
# my_gallows.restart()
# my_gallows.play("new word")
# print(my_gallows.game_over)
# # False
# # ['apple']
# # ['apple']
# # ['apple', 'ear']
# # game over
# # True
# # False
