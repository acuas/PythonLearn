#Importing random module to use choice function
import random

print("\tWelcome to 'Guess the word' game!")
print("\nYou have only five chances to ask if a letter is in the word or not")

#Initializate a tuple with words
WORDS = ("masina", "cumparaturi", "vacanta", "multe", "browser")
#Randomly choice a word from the tuple
word = random.choice(WORDS)
print("The word has", len(word), "letters!")

for i in range(5):
   letter = input("Enter the letter that you want to know if it's in the word or not : ")
   if letter in word:
       print("yes")
   else:
       print("no")

guess = input("Enter a word : ")

if guess == word:
    print("You have guessed the word!")
else:
    print("You haven't guessed the word!") 

input("Press the enter key to exit!\n")
