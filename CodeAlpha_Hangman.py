import random


words = [
    "python",
    "computer",
    "programming",
    "developer",
    "algorithm",
    "database",
    "keyboard",
    "internet",
    "software",
    "github"
]


word = random.choice(words)


guessed_letters = []


lives = 6

print("==============================")
print("       HANGMAN GAME")
print("==============================")

# Game loop
while lives > 0:

    
    print("\nWord: ", end="")

    for letter in word:

        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    print("Lives remaining:", lives)

    
    guess = input("Enter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    
    guessed_letters.append(guess)

    
    if guess in word:
        print("Correct guess! ")

    else:
        print("Wrong guess! ")
        lives -= 1

    
    word_guessed = True

    for letter in word:
        if letter not in guessed_letters:
            word_guessed = False
            break

    if word_guessed:
        print("\n🎉 YOU WON!")
        print("The word was:", word)
        break


if lives == 0:

    print("\n💀 GAME OVER!")
    print("The word was:", word)

print("==============================")
