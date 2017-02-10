# Kristian Snyder
# Homework 1
# 10 February 2017

"""The Game of Hog."""

from extra import *
from dice import four_sided, six_sided, make_test_dice
from math import log10

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def bacon(score):
    return max([int(i) for i in str(score)]) + 1

def roll_dice(num_rolls, dice=six_sided):
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    rolls = []
    for roll in range(0, num_rolls):
        rolls.append(dice())
    if 1 in rolls:
        return 1
    else:
        return sum(rolls)
    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    if num_rolls == 0:
        return bacon(opponent_score)
    return roll_dice(num_rolls, dice)
    # END Question 2

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    return six_sided if (score + opponent_score) % 7 != 0 else four_sided
    # END Question 3

def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    # First item is the tens digit, second item is the ones digit.
    # Sometimes the result of dividing by 10 is more than 10, so
    # need to take the modulo of it.
    score0 = set(((score0 // 10) % 10, score0 % 10))
    score1 = set(((score1 // 10) % 10, score1 % 10))
    # Sets are compared without respect to order
    if score0 == score1:
        return True
    return False
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    # allows for indexing based on who
    scores = [score0, score1]
    strategies = (strategy0, strategy1)

    while scores[0] < goal and scores[1] < goal:
        # storing opponent number for easy reference later
        opponent = other(who)
        # get the correct dice
        dice = select_dice(scores[who], scores[opponent])
        # get the score result for the player's roll and add to the player's score
        scores[who] += take_turn(strategies[who](scores[0], scores[1]),
                                 scores[opponent], dice)
        # pass both scores to the is_swap function to see if we should swap
        if is_swap(scores[0], scores[1]):
            # basic swap routine
            temp = scores[0]
            scores[0] = scores[1]
            scores[1] = temp
        # set next player to the opposite one
        who = other(who)
    score0, score1 = scores[0], scores[1]
    # END Question 5
    return score0, score1

###### READ NOTE BELOW ######
# NOTE: the below function replaces the main function that was not included
#       and correctly passes the argument to run() in extra.py.

if __name__ == '__main__':
    import sys
    run(*sys.argv[1:])
