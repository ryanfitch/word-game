import random

word_list = ['apple', 'banana', 'cantaloupe', 'date', 'elderberry', 'fig']
lives = 3
characters = []
game_output = []

def main():
  running = True

  def welcome():
    print ("\nWelcome to the word game!")
    print ("See if you can guess the word one letter at a time.\n")

  def get_word():
    # eventually get a random word from a list of words
    return word_list[random.randint(0, len(word_list)-1)]

  def again():
    again = input("Would you like to play again?  y/n: ")
    if again == 'y':
      main()
    elif again == 'n':
      print("Goodbye")
      exit()
    else:
      print("I didn't understand that input.  Please try again.")
      again()

  def split_word(_word):
    return list(_word)

  def create_game(list_of_characters):
    new_game = ['_ '] * len(list_of_characters)
    return new_game

  def check_guess(_input):

    for i, letter in enumerate(characters):
      if _input == letter:
        game_output[i] = _input

  def check_game_state():
    score = 0
    guesses = 0
    for i, letter in enumerate(characters):
      if game_output[i] == letter:
        score += 1
      else:
        guesses += 1
    if score == len(characters):
      finishedWord = ''.join(game_output)
      print ("Nice job!  You figured out the word was {}.".format(finishedWord))
      again()
      # return False
    else:
      print("Letters right: {}\nLetters left: {}".format(score, guesses))
      return True


  characters = split_word(get_word())
  game_output = create_game(characters)

  welcome()
  print("Make a guess: ")
  print(game_output)

  while running:
    _input = input()
    check_guess(_input)
    print(game_output)
    running = check_game_state()

main()
