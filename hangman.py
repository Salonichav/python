
word_list = ["apple", "banana", "carrot"]
import random
chosen_word = random.choice(word_list)

lives = 6

print(f'Pssstt, the solution is {chosen_word}.')
display = []
word_lenght = len(chosen_word)
for _ in range(word_lenght):
   display+= "_"
   print(display)

end_of_game = False
while  end_of_game:

   guess = input("Guess a letter:").lower()
for position in range(word_lenght) :
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
    if guess not in chosen_word:
      lives == 0
      end_of_game = True
      print("You Win.")



      print(f"{''.join(display)}")

      if "_" not in display:
        end_of_game = True
        print ("You win!.")
       

