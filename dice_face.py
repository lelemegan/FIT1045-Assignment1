import random
def roll_dice(num_of_dice=1):
  """
  Pick random numbers based on the number of dice being inputted

  Arguments:
    - num_of_dice: Accepts int. This is the number of dice to be rolled.

  Return Value:
    - A list of 2 elements, 
      - roll result as a list of integer in position 0, 
      - Ascii art for dice face in string in position 1

  Implemented by:
    - Jinwei Liang 30741424
  """

  # Pick random number form the die
  roll_results = []
  for i in range(num_of_dice):
    roll = random.randint(1, 6)
    roll_results.append(roll)

  # Generate the Diagram of Dice Faces
  die_art = {
      1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
      2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
      3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
      4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
      5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
      6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
    }
  dice_row = []
  dice_row_to_str =''
  show_dice_face = ''
  # Go thought each row of dice
  for row_of_dice in range(5):
      temporary_storage = []
      # Go thought each dice
      for number_of_dice in range(len(roll_results)):
          x = roll_results[number_of_dice]
          temporary_storage.append(die_art[x][row_of_dice])
      # Combine same row for all dice
      dice_row_to_str = ' '.join(temporary_storage)
      dice_row.append(dice_row_to_str)
  # Combin final result
  show_dice_face = '\n'.join(dice_row)


  return [roll_results, show_dice_face]
#raise NotImplementedError

