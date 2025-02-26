import random
from art import stages,logo
from words import word_list
print(logo)
lives = 0

chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for position in range(len(chosen_word)):
    placeholder  += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"----------{lives}/6 times attempted.")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(g uess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives += 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        if lives == 6:
            game_over = True
            print(f"----------The word was {chosen_word}. You lose----------.")

    if "_" not in display:
        game_over = True
        print("----------You win----------.")

    print(stages[lives])