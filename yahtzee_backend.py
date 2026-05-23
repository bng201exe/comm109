import random

def init_game():
    game_state = {}
    game_state['player'] = "?"
    game_state['round'] = 1
    game_state['roll'] = 1
    game_state['status'] = 'WAIT_FOR_ROLL'
    game_state['dice']   = [ '-', '-', '-', '-', '-'] 
    game_state['locked'] = [ False, False, False, False, False ]
    game_state['1'] = None
    game_state['2'] = None
    game_state['3'] = None
    game_state['4'] = None
    game_state['5'] = None
    game_state['6'] = None
    game_state['T'] = None
    game_state['F'] = None
    game_state['H'] = None
    game_state['S'] = None
    game_state['L'] = None
    game_state['C'] = None
    game_state['Y'] = None
    game_state['UPPER TOTAL'] = 0
    game_state['BONUS'] = 0
    game_state['LOWER TOTAL'] = 0
    game_state['TOTAL SCORE'] = 0
    return game_state
 
upper_rows =  [ '1', # ONES'
                '2', # TWOS'
                '3', # THREES'
                '4', # FOURS'
                '5', # FIVES'
                '6'] # SIXES'
 
lower_rows = [ 'T', # THREE OF A KIND'
               'F', # FOUR OF A KIND'
               'S', # SHORT STRAIGHT'
               'L', # LONG STRAIGHT'
               'H', # FULL HOUSE'
               'C', # CHANCE'
               'Y'] # YAHTZEE' 

misc_rows = ['UPPER TOTAL',
             'BONUS', 
             'LOWER TOTAL',
             'TOTAL SCORE' ]

char_to_row =  { '1': 'ONES',
                 '2': 'TWOS',
                 '3': 'THREES',
                 '4': 'FOURS',
                 '5': 'FIVES',
                 '6': 'SIXES',
                 'T': 'THREE OF A KIND',
                 'F': 'FOUR OF A KIND',
                 'S': 'SHORT STRAIGHT',
                 'L': 'LONG STRAIGHT',
                 'H': 'FULL HOUSE',
                 'C': 'CHANCE',
                 'Y': 'YAHTZEE' }

row_to_char = { 'ONES': '1',
                'TWOS': '2',
                'THREES': '3',
                'FOURS': '4',
                'FIVES': '5',
                'SIXES': '6',
                'THREE OF A KIND': 'T',
                'FOUR OF A KIND': 'F',
                'SHORT STRAIGHT': 'S',
                'LONG STRAIGHT': 'L',
                'FULL HOUSE': 'H',
                'CHANCE': 'C',
                'YAHTZEE': 'Y'}




def score_upper_section(dice, val):
    score = 0
    for i in dice:
        if i == val:
            score += i

    return score


def score_3_of_a_kind(dice):
    score = 0
    counts = []
    dice_copy = dice[:]
    for i in range(1,7):
        if i in dice_copy:
            counts.append(dice_copy.count(i))
    
    for i in counts:
        if i >= 3:
            three_sum = sum(dice)
            score += three_sum
            break
    
    return score


def score_4_of_a_kind(dice):
    score = 0
    counts = []
    dice_copy = dice[:]
    for i in range(1,7):
        if i in dice_copy:
            counts.append(dice_copy.count(i))
    
    for i in counts:
        if i >= 4:
            four_sum = sum(dice)
            score += four_sum
            break
    return score



def score_short_straight(dice):
    score = 0
    dice_copy = dice[:]
    short_straight_dice = sorted(set(dice_copy))
    short_straight1 = [1,2,3,4]
    short_straight2 = [2,3,4,5]
    short_straight3 = [3,4,5,6]
    if short_straight_dice[0:4] == short_straight1:
        score = 30 
    if(short_straight_dice[0:4] == short_straight2) or (short_straight_dice[1:5] == short_straight2):
        score = 30
    if(short_straight_dice[0:4] == short_straight3) or (short_straight_dice[1:5] == short_straight3):
        score = 30
    

    return score


def score_long_straight(dice):
    score = 0
    dice_copy = dice[:]
    sorted_dice = sorted(dice_copy)
    if sorted_dice == [1,2,3,4,5]:
        score = 50
    if sorted_dice == [2, 3, 4, 5, 6]:
        score = 50
    return score


def score_full_house(dice):
    score = 0
    counts = []
    dice_copy = dice[:]
    for i in range(1,7):
        if i in dice_copy:
            counts.append(dice_copy.count(i))
    if (3 in counts) and (2 in counts):
        score += 25 
    
    return score


def score_chance(dice):
    score = 0
    score += sum(dice)
    return score


def score_yahtzee(dice):
    score = 0
    dice_copy = dice[:]
    dice_set = set(dice_copy)
    if len(dice_set) == 1:
        score = 50
    
    return score


def initialise_game():
    game_state = {}
    return game_state
    

def roll_dice(game_state):
    indices = []
    locked_copy = game_state["locked"[:]]
    for i in range(5):
        if locked_copy[i] == False:
            indices.append(i)
    print(indices)
    for i in indices:
        roll = random.randint(1,6)
        game_state["dice"[i]] = roll
        
    return


def reset_dice(game_state):
    game_state["dice"] = ["-", "-", "-", "-", "-"]
    game_state["locked"] = [False, False, False, False, False]
    return


def lock_dice(game_state, dice_to_keep):
    return success


def toggle_dice(game_state, idx):
    dice_to_toggle = 
    return


def get_score(game_state, row_char):
    score = 0
    return score


def update_scorecard(game_state, row_char):
    return True


# optional extensions

def load_existing_game(game_state):
    loaded_game = False
    return loaded_game


def save_score(game_state):
    return


def get_stats(game_state):
    formatted_stats = ""
    return formatted_stats
    