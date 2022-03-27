green = '\33[102m'
yellow = '\33[43m'
reset = '\033[0m'

word = ['G', 'R', 'E', 'A', 'T']

def displayWords(word):
    color = reset
    for index, letter in enumerate(word):
        if letter in word:
            if letter == word[index]:
                color = green
            else:
                color = yellow
        print(f"{color}{letter}{reset}")


guessed = input("Word - ").upper()
guessed_word = list(guessed)

print(guessed_word)

displayWords(guessed_word)

print(f"{green}Hello{reset}")