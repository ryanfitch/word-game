word_list = ['apple']
lives = 3
characters = []
game_output = []

win = False


def get_word():
  # eventually get a random word from a list of words
  return word_list[0]

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
    return True
  else:
    return False


characters = split_word(get_word())
game_output = create_game(characters)

print("Make a guess: ")
print(game_output)

while win == False:
  _input = input()
  check_guess(_input)
  print(game_output)
  win = check_game_state()




