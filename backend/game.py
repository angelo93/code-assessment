from random import randrange

# ********************************************************************
# NOTES
# ********************************************************************
# Python has an interesting approach to Enums compared to C.
# My original intent was to use enums since they are lightweight.
# Due to the more robust nature of Python enums, I decided to use globals.
# The utilization of a number is to speed up comparisons

# ********************************************************************
# GLOBALS
# ********************************************************************
RES_TIE = 0
RES_PLR_ONE = 1
RES_PLR_TWO = 2

MODE_PVP = 0
MODE_PVC = 1

CHOICE_ROCK = 0
CHOICE_PAPER = 1
CHOICE_SCISSORS = 2

CHOICES = {CHOICE_ROCK: "rock",
           CHOICE_PAPER: "paper",
           CHOICE_SCISSORS: "scissors"}
RESULTS = {RES_TIE: "It's a Tie!",
           RES_PLR_ONE: "Player One Wins!",
           RES_PLR_TWO: "Player Two Wins!"}


# ********************************************************************
# GAME LOGIC
# ********************************************************************
def get_result(plr_one_choice: int, plr_two_choice: int):
    '''
    Action: Get result of match, assume player two wins
    Params: Player one and two choices
    Return: Match result
    Note:   Assuming a default state allows for a smaller number of checks
    '''
    result = RES_PLR_TWO

    if plr_one_choice == plr_two_choice:
        result = RES_TIE
    elif plr_one_choice == CHOICE_ROCK and plr_two_choice == CHOICE_SCISSORS:
        result = RES_PLR_ONE
    elif plr_one_choice == CHOICE_PAPER and plr_two_choice == CHOICE_ROCK:
        result = RES_PLR_ONE
    elif plr_one_choice == CHOICE_SCISSORS and plr_two_choice == CHOICE_PAPER:
        result = RES_PLR_ONE
    else:
        # MISRA
        pass
    # end if

    return result
# end get_result()


def match_result(plr_one_choice: int, plr_two_choice: int, mode: int):
    '''
    Action: Get result of match
    Params: Player one and two choices, mode: game mode
    Return: Match result information
    '''
    if mode == MODE_PVC:
        plr_two_choice = randrange(0, len(CHOICES))
    # end if

    result = {"plr_one_choice": CHOICES[plr_one_choice],
              "plr_two_choice": CHOICES[plr_two_choice]}

    result["result"] = get_result(plr_one_choice, plr_two_choice)
    result["msg"] = RESULTS[result["result"]]

    return result
# end match_result()
