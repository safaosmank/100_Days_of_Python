import random

import hangman_word
import hangman_art

end_game = False
lives = 6

chosen_word = random.choice(hangman_word.word_list)

print(hangman_art.logo)

#create a blank list
display = []
for i in chosen_word:
  display += "_"



end_game = False
while not end_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"you've already guessed {guess}")
  for position in range(len(chosen_word)):
    i = chosen_word[position]
    if guess in i:
      display[position] = i



  if guess not in chosen_word:
    lives -=1
    print(f"you choose letter {guess} , that is not in the word. You lose a life")
    if lives == 0:
      end_game =True
      print("You lose")

  print(f"{''.join(display)}")
  if "_" not in display:
    end_game = True
    print("You Win")

  print(hangman_art.stages[lives])


