import random

word_list = ['apple', 'banana', 'cantaloupe', 'date', 'elderberry', 'fig']
lives = 3
characters = []
game_output = []

running = True


def get_word():
  # eventually get a random word from a list of words
  return word_list[random.randint(0, len(word_list)-1)]

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
  for i, letter in enumerate(characters):
    if game_output[i] == letter:
      score += 1
  if score == len(characters):
    return False
  else:
    return True


characters = split_word(get_word())
game_output = create_game(characters)

print("Make a guess: ")
print(game_output)

while running:
  _input = input()
  check_guess(_input)
  print(game_output)
  running = check_game_state()
