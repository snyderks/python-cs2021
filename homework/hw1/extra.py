# Kristian Snyder
# Homework 1
# 10 February 2017

from dice import *
from hog import *

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    # BEGIN Question 6
    def average(*args):
        total = 0
        # loops through and calls the function each time.
        # could also be accomplished with avg() and a list comprehension.
        for _ in range(0, num_samples):
            total += fn(*args)
        return total / num_samples
    return average
    # END Question 6

def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    average = make_averaged(roll_dice, num_samples)
    # list of averages for each number of dice
    averages = [average(i, dice) for i in range(1, 11)]
    max_value = max(averages)
    # as index enumerates through the list in ascending order, we'll get
    # the lowest dice number first if it's a duplicate.
    max_index = averages.index(max_value)
    return max_index + 1 # offset zero-based indexing
    # END Question 7

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if True: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True: # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    # testing final strategy
    maxWin = 0
    for _ in range(0, 20):
        win = average_win_rate(final_strategy)
        maxWin = win if win > maxWin else maxWin
    print('best final_strategy win rate out of 20:', maxWin)


    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    if bacon(opponent_score) >= margin:
        return 0
    return num_rolls
    # END Question 8

def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS if rolling 0 dice results in a harmful swap. It also
    rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
    otherwise.
    """
    # BEGIN Question 9
    # determine if rolling a 0 results in a swap
    swap = is_swap(score + bacon(opponent_score), opponent_score)
    # beneficial swap
    if swap and score < opponent_score:
        return 0
    # detrimental swap
    elif swap and score > opponent_score:
        return num_rolls
    # no swap OR neutral swap
    else:
        return bacon_strategy(score, opponent_score, margin, num_rolls)
    # END Question 9

def final_strategy(score, opponent_score):
    """This strategy makes a few decisions:
    If it can win with a bacon, it does.
    If it is more than 10 points ahead and can give the opponent four-sided
    dice with a bacon, it does.
    It will roll 1 fewer dice if they are four-sided.
    The default margin for swap_strategy to beat is 9 points, with two
    subtracted for four-sided dice.
    """
    # BEGIN Question 10
    # first line: wins through bacon if possible
    # second and third lines: gives opponent four_sided dice if more than 10 pts ahead
    if GOAL_SCORE - score <= bacon(opponent_score) and not is_swap(score, opponent_score) or \
       score > opponent_score + 10 and select_dice(score + bacon(opponent_score),
                                                  opponent_score) is four_sided:
        return 0

    # reduce roll if using four-sided dice
    rollOffset = -1 if select_dice(score, opponent_score) is four_sided else 0

    # default roll is 5
    roll = 5 + rollOffset

    # determine if the margin score is better than could be done with a bacon roll
    # take off two from the margin for four-sided dice
    return swap_strategy(score, opponent_score, 9 + rollOffset * 2, roll)
    # END Question 10


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.

###### READ NOTE BELOW ######
# NOTE: I have removed the decorator on run(), as the correct function was not included.

def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--final', action='store_true',
                        help='Display the final_strategy win rate against always_roll(5)')
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
    elif args.final:
        from hog_eval import final_win_rate
        win_rate = final_win_rate()
        print('Your final_strategy win rate is')
        print('    ', win_rate)
        print('(or {}%)'.format(round(win_rate * 100, 2)))
