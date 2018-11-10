""" Maxwell Hunter - 11/10/18
Going over everything with a pep8 linter, everything has much better
aesthetics. fixed a few typos too.
"""

""" Maxwell Hunter - 8/24/18

The Challenge text:
Write a python module which implements a Game class that scores a bowling game
(see http://bowling.about.com/od/rulesofthegame/a/bowlingscoring.htm for a
description of how bowling is scored).

The class should provide two ways to calculate a bowling game score:

From an optional argument to the class initializer: a string between 12 and 21
characters long where each character represents a throw: X for a strike,
/ for a spare, or a number indicating how many pins were knocked down.

Real time: The Game class should define a function that takes a single
argument indicating the score of one throw,
and returns the running score for the whole game.
The Game class should define a property which contains the
calculated score of the game.
"""


def x_if_strike(score_str):
    if score_str == 10:
        return 'X'
    else:
        return score_str


def add_spare_bonus(next_throw):
    # tracking a spare, we get 10 for the frame + the pins from the next thow.
    bonus_score = 10
    # if next throw is a strike,
    if next_throw[0] == "X":
        # then add 10
        bonus_score += 10
    # otherwise, add the next throw
    else:
        # then add as a bonus
        bonus_score += int(next_throw[0])
    # return the total frame score for the spare + the bonus
    return bonus_score


# calculates just the strike bonus, using the next two throws
def add_strike_bonus(next_two_throws):
    # by looking at the second to next throw first,
    # we can deduce the total bonus easier

    # track bonus score, starting with the strike we got
    bonus_score = 10
    # if the second next throw is a number, ('X?#')
    if next_two_throws[1].isdigit():
        # add that number to the frame score
        bonus_score += int(next_two_throws[1])
        # if first next throw is also a strike ('XX#')
        if next_two_throws[0] == "X":
            # add 10 to bonus
            bonus_score += 10
        # the first next throw has to be a number if it's not a strike. ('X##')
        # because it can't be a spare
        else:
            # so add it to the bonus
            bonus_score += int(next_two_throws[0])
    # if the second next throw is a strike ('X?X')
    elif next_two_throws[1] == "X":
        # then add 10 to the bonus and keep going
        bonus_score += 10
        if next_two_throws[0] == "X":
            # if first next throw is also strike, ('Turkey')
            # then add 10 again
            bonus_score += 10
        # if first next throw is a number, ('XX?')
        else:
            # then add to bonus
            bonus_score += int(next_two_throws[0])
    # if second next throw is a spare,
    elif next_two_throws[1] == "/":
        # add 10 and stop
        bonus_score += 10
    # return the total bonus
    return bonus_score


# translate characters are strikes (x, X) returns boolean
def is_strike(char):
    if char in ['x', 'X']:
        return True
    else:
        return False


def is_spare(char):
    if char == '/':
        return True
    else:
        return False


def print_scoreboard(frame_list, score_list, frame_idx, throw_number):
    # build the gameboard in a graphical display

    for i in range(1, 13):
        print "-",
    else:
        print
    print "|  SCOREMASTER 9000   |"
    for i in range(1, 13):
        print "-",
    else:
        print
    for i in range(1, 11):
        print " ----- ",
    else:
        print

    for i in range(1, 10):
        if i == frame_idx+1:
            print "[ >{}< ]".format(i),
        else:
            print "[  {}  ]".format(i),
    else:
        print '[ 10  ]'

    for i in range(1, 11):
        print " ----- ",
    else:
        print

    # print out each frame in the game in order left to right,
    # and display scores for frames that have already been played
    for i, frame in enumerate(frame_list):
        # if the frame has been played
        if i < frame_idx:
            if i == 9:
                print '[{},{},{}]'.format(
                    x_if_strike(
                        frame[0]
                        ),
                    x_if_strike(
                        frame[1]
                        ),
                    x_if_strike(
                        frame[2]
                        )
                    ),
            # if the total is 10
            elif sum(frame) == 10:
                # if the first throw in the frame is (it's a strike)
                if frame[0] == 10:
                    # display a strike
                    print '[ -,X ]',
                # if the first throw is not 10, it's a spare
                else:
                    # display a spare
                    print '[ {},/ ]'.format(frame[0]),
            # if the frame total is not 10
            else:
                print '[ {},{} ]'.format(frame[0], frame[1]),
        # if the frame is currently being played
        elif i == frame_idx:
            # if it's the tenth frame
            if i == 9:
                # if it's the first throw
                if throw_number == 0:
                    print '[*, , ]',
                # if it's the second throw
                elif throw_number == 1:
                    print '[{},*, ]'.format(
                        x_if_strike(
                            frame[0]
                            ),
                        ),
                # if it's the third throw
                elif throw_number == 2:
                    print '[{},{},*]'.format(
                        x_if_strike(
                            frame[0]
                            ),
                        x_if_strike(
                            frame[1]
                            ),
                    ),
            # if it's the first nine frames
            else:
                # if it's the second throw
                if throw_number == 1:
                    print '[ {},* ]'.format(frame[0]),
                # if it's the first throw
                else:
                    print '[ *,  ]',
        elif i < 9:
            print '[  ,  ]',
        elif i == 9:
            print '[ , , ]',
    print

    # underneith that, display the running total score
    for i in range(0, 10):
        # if the frame has been played
        if i < frame_idx:
            # load running total
            running_total = sum(score_list[0:i+1])
            # convert the number to a string
            frame_string = str(running_total)
            # in order to keep the numbers aligned, print the number centered
            if len(frame_string) == 3:
                print "[", frame_string, "]",
            elif len(frame_string) == 2:
                print "[ ", frame_string, "]",
            else:
                print "[ ", frame_string, " ]",
        # if the frame hasn't been played yet,
        else:
            # print an empty string
            print "[     ]",
    else:
        print
    for i in range(1, 11):
        print " ----- ",
    else:
        print


def calculate_finished_game(score_string):
    # track running score
    score = 0
    # track which frame we're on
    frame_idx = 0
    # track which throw we're on
    throw_number = 0
    # track if there's an extra throw this frame
    is_bonus_throw = False
    # add end characters, so the bonus doesn't loop and start from beginning
    score_string += '<<<'
    # covert the string to a list to make it easier to iterate
    score_list = list(score_string)
    # create a list of each frame, and what they scored
    frame_list = []
    for i in range(0, 10):
        frame_list.append([0, 0])
    # add the special 10th frame
    frame_list.append([0, 0, 0])
    # create a list of the total scores for the frame
    score_list = [0]*12

    for idx, throw in enumerate(score_string):
        # if we encounter the end charactures, break the loop
        if throw == '<':
            break
        if frame_idx < 10:
            if throw.isdigit():
                # if next throw is a spare,
                if score_string[idx+1] == "/":
                    # add the throw to the frame_list
                    frame_list[frame_idx][0] = int(throw)
                # if it's a normal throw,
                else:
                    # just add to the frame score
                    score_list[frame_idx] += int(throw)
                    # add to the running score also
                    score += int(throw)
                    if not is_bonus_throw:
                        throw_number += 1
                        is_bonus_throw = True
                    else:
                        # move to the next frame
                        throw_number = 0
                        frame_idx += 1
                        is_bonus_throw = False

                frame_list[frame_idx][throw_number] = int(throw)
            # if the throw is a srike,
            elif is_strike(throw):
                # calculate the strike using the next two throws as well
                strike_bonus = add_strike_bonus(score_string[idx+1:idx+3])
                # add that value to the frame score
                score_list[frame_idx] += strike_bonus
                frame_list[frame_idx][throw_number] = 10
                # add that also to the strike bonus
                score += strike_bonus
                # move to the next frame
                frame_idx += 1
            elif is_spare(throw):
                # set frame score to 10 + next throw
                # no matter what the first throw was (can only be a number,
                # (can't throw two spares in a row, or a spare after a strike))
                spare_bonus = add_spare_bonus(score_string[idx+1:idx+2])
                # set frame score to that value
                score_list[frame_idx] = spare_bonus
                frame_list[frame_idx][
                    throw_number] = 10 - frame_list[frame_idx][0]
                # add that also to the strike bonus
                score += spare_bonus
                # move to the next frame
                frame_idx += 1
    return score


def check_valid_throw(throw, pins):
    # if input is a number (only numbers are accepted)
    if not throw.isdigit():
        return False
    # check that the number isn't greater than the number of pins abailable
    if int(throw) > pins:
        print "no you didn't! there aren't that many pins left."
        return False
    else:
        return True


def reset_pins(pins=0):
    return 10


def calculate_unfinished_game(test_string=""):
    """ a real-time function that takes user input as the game progresses. """
    # get user input
    print "No old game entered, starting new Game"
    # which frame we're on,
    # which throw we're on in the frame,
    # and the number of throws so far
    # throw_number checks which throw in the frame you're on,
    # throw_idx tracks the number of throws so far total.
    frame_idx = throw_number = throw_idx = 0

    # track if there's an extra throw this frame, only used in 10th frame
    bonus_throw = False
    # create a list of throws as they come in
    throw_list = []
    # create a list of each frame, and what they scored -
    frame_list = []
    # and add the first 9 frames
    for _ in range(0, 9):
        frame_list.append([0, 0])

    # add the special 10th frame
    frame_list.append([0, 0, 0])
    # create a list of the total scores for the frame
    score_list = [0]*10
    # track the number of pins standing
    pins = reset_pins()
    # track which throw goes to which frame
    throw_to_frame = {}

    if test_string:
        test_list = list(test_string)

    # while - a game of bowling has only 10 frames
    while frame_idx < 10:
        print
        # just to add two lines between throws
        print

        print_scoreboard(frame_list, score_list, frame_idx, throw_number)
        print """You are on frame {} and are on your throw {}.
Your running score is {}. There are {} pins standing.""".format(
            # show which frame
            frame_idx+1,
            # show throw they're on
            throw_number+1,
            # show their score
            sum(score_list),
            # show how many pins are standing
            pins,
            )

        print
        # just to add two lines between throws
        print

        # just for testing: convert X to 10
        if test_string:
            throw = test_list.pop(0)
            if throw == 'X':
                throw = '10'
        else:
            # get user input
            throw = raw_input("After your throw, enter a number 0-10. > ")
        # along with numbers for pins, we can also accept characters
        # x, X & / (for strikes and spares)
        if not throw.isdigit():
            # covert X to strike
            if is_strike(str(throw)):
                throw = '10'
            # covert / to spare
            if is_spare(str(throw)):
                # if we're on the first throw
                if not throw_number:
                    print 'Cannot get spare on first throw!'
                    continue
                else:
                    throw = str(10-throw_list[throw_idx-1])

        # check that the number isn't greater than the number of pins abailable
        if not check_valid_throw(throw, pins):
            print "Enter only numbers, please."
            # if it's invalid, try again
            continue
        # cast to int
        throw = int(throw)
        # save throw in throw_list
        throw_list.append(throw)
        # save which throw was in which frame
        throw_to_frame[str(throw_idx)] = frame_idx
        # save throw score into the throw score sheet
        frame_list[frame_idx][throw_number] = throw
        # save throw into the frame score sheet
        score_list[frame_idx] += throw
        # update how many pins are standing after the throw
        pins -= throw

        # check for strikes and spares
        # if we can check last throw
        if len(throw_list) > 1:
            # if last throw was a strike
            if throw_list[throw_idx-1] == 10:
                # if last frame was in the first 9
                if throw_to_frame[str(throw_idx-1)] < 9:
                    # add this throw to the frame for that throw
                    score_list[throw_to_frame[str(throw_idx-1)]] += throw
            elif throw_number < 1:
                # if last frame was a spare
                if score_list[frame_idx-1] == 10:
                    # add this throw to last frame
                    score_list[frame_idx-1] += throw
        # if we can check two throws ago
        if len(throw_list) > 2:
            # if second to last throw was a strike
            if throw_list[throw_idx-2] == 10:
                # if second to last frame was in the first 9
                if throw_to_frame[str(throw_idx-2)] < 9:
                    # add this throw to the score from that frame
                    score_list[throw_to_frame[str(throw_idx-2)]] += throw

        # what to do after the throw depends on several factors
        # first nine frames
        if frame_idx < 9:
            # first throw
            if throw_number < 1:
                # if there are pins left
                if pins > 0:
                    # go to second throw in frame
                    throw_number += 1
                # if there are no pins left
                else:
                    print "Strike!"
                    print
                    # reset pins
                    pins = reset_pins(pins)
                    # go to next frame
                    frame_idx += 1
                    throw_number = 0
            # second throw
            else:
                # if there are pins left
                if pins == 0:
                    print "Spare!"
                    print
                # go to next frame
                frame_idx += 1
                # reset throw_number to 0
                throw_number = 0
                # reset pins
                pins = reset_pins(pins)
        # final 10th frame
        else:
            # first throw
            if throw_number < 1:
                # if there no are pins left
                if pins == 0:
                    print "Strike!"
                    print
                    # reset pins
                    pins = reset_pins(pins)
                    # you get a bonus 3rd throw
                    bonus_throw = True
            # second throw
            elif throw_number < 2:
                # if there no are pins left
                if pins == 0:
                    # if last throw was a strike,
                    if throw_list[throw_idx-1] == 10:
                        print "Strike!"
                        print
                    # if last throw was not a strike,
                    else:
                        print "Spare!"
                        print
                    # either way, you get a bonus 3rd throw
                    bonus_throw = True
                # reset pins
                pins = reset_pins(pins)
                # if you don't have a bonus throw
                if not bonus_throw:
                    # go to next frame, ends the game
                    frame_idx += 1
            # third throw
            elif throw_number < 3:
                # go to next frame, ends the game
                frame_idx += 1
            # increment throw_number
            throw_number += 1
        # increment throw_idx
        throw_idx += 1

    print_scoreboard(frame_list, score_list, frame_idx, throw_number)

    if not test_string:
        _ = raw_input("Game Over!")
        print "  {}".format(_)
        print
        print "final score: {}".format(sum(score_list))
        if raw_input(
            """Play again? Enter 'Y' to play again,
                or press enter to quit. """).lower() == 'y':
            Game()                                    # pragma: no cover
    return sum(score_list)


class Game(object):
    score = 0

    def __init__(self, score_string=""):
        """docstring for Game
        #Class should provide two ways to calculate a bowling game score:
        1. From an optional argument to the class initializer:
        2. Real time: The Game class should define a function that takes
        a single argument indicating the score of one throw,
        and returns the running score for the whole game.
        """

        # if an argument was entered,
        if score_string != "":
            # calculate using the finished game method
            self.score = calculate_finished_game(score_string)
        # if an argument was not entered,
        else:
            # calculate using the unfinished game method (collects user input)
            self.score = calculate_unfinished_game()


if __name__ == '__main__':
    Game()  # pragma: no cover
