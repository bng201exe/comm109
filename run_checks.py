from yahtzee_backend import *
from yahtzee_game import * 

# run a check on the score_3_of_a_kind
# in this case when coded the correct result should be 25

mydice = [6,6,6,5,2]
result = score_upper_section(mydice,6)
print(f"running  on {mydice} ... result is {result}")

mydice2 = [6,6,3,5,5]
result = score_3_of_a_kind(mydice2)
print(f"running  on {mydice2} ... result is {result}")

mydice3 = [5,2, 2, 2, 2]
result = score_4_of_a_kind(mydice3)
print(f"running  on {mydice3} ... result is {result}")

mydice4 = [1, 1, 1, 6, 6]
result = score_full_house(mydice4)
print(f"running  on {mydice4} ... result is {result}")

mydice5 = [2,3,4,5,6]
result = score_long_straight(mydice5)
print(f"running  on {mydice5} ... result is {result}")

mydice6 = [2,2,4,5,6]
result = score_short_straight(mydice6)
print(f"running  on {mydice6} ... result is {result}")

mydice7 = [2,2,4,5,6]
result = score_chance(mydice7)
print(f"running  on {mydice7} ... result is {result}")

mydice8 = [6,6,6,6,6]
result = score_yahtzee(mydice8)
print(f"running  on {mydice8} ... result is {result}")

roll_dice(game_state)


#game_state = init_game()
#game_state['locked'] = []
#print(game_state)
#roll_dice(game_state)
#print(game_state)
#display_game_state_debug(game_state)
#print(game_state['locked'])
#print(game_state['dice'])