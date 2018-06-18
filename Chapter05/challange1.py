# A program that prints a list of words in random order
import random
# The list of words that will be displayed in random order
WORDS = ["consider", "minute", "accord", "evident"]
c_words = WORDS[:]
n = len(c_words)
for i in range(0, n):
    word = random.choice(c_words)
    print(word, end=" ")
    c_words.remove(word)

input("\n\nPress the enter key to exit!")

