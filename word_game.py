word_list = ['apple']
lives = 3
characters = []
game_output = []


def get_word():
  return word_list[0]

def split_word(_word):
  return list(_word)

def get_length(_characters):
  return len(_characters)

def create_game(list_of_characters):
  new_game = '_ ' * len(list_of_characters)
  return new_game

#def check_characters(_input):
#  index = 0
#  for i in characters:
#    if i == _input:

characters = split_word(get_word())
game_output = create_game(characters)
print("Make a guess: ")
print(game_output)

while lives > 0:


  # print("make a guess")
  # print(": ")

  # print (get_length(guess))


