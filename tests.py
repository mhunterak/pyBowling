# import unittest framework
import unittest
# import the script we're testing
import bowling


# define functions for testing

# tests finished games with input strings
def testFinishedGame(self, inputString, expectedScore):
    self.assertEqual(bowling.calculate_finished_game(
        inputString), expectedScore)
    self.assertEqual(bowling.Game(inputString).score, expectedScore)


# tests unfinished games using a single character as the input for every throw
def testUnfinishedGameWithRawInputs(self, inputString, expectedScore):
    originalRawInput = __builtins__.raw_input
    __builtins__.raw_input = lambda _: inputString
    self.assertEqual(bowling.Game().score, expectedScore)
    __builtins__.raw_input = originalRawInput


'''
# tests unfinished games using a string -
like the finished game method does, but using the function players use to play
an unfinished game.
'''


def testUnfinishedGameWithStrings(self, inputString, expectedScore):
    self.assertEqual(bowling.calculate_unfinished_game(
        inputString), expectedScore)


# test finished games, with input strings
class TestFinishedGameMethods(unittest.TestCase):
    def testFinishedGame_PerfectGame(self):
        testFinishedGame(self, 'XXXXXXXXXXXX', 300)

    def testFinishedGame_NoStrikesGame(self):
        testFinishedGame(self, '90909090909090909090', 90)

    def testFinishedGame_SparesGame(self):
        testFinishedGame(self, '5/5/5/5/5/5/5/5/5/5/5', 150)

    def testFinishedGame_RandomOneGame(self):
        testFinishedGame(self, 'X7/729/XXX236/7/3', 168)

    def testFinishedGame_GutterballGame(self):
        testFinishedGame(self, '00000000000000000000', 0)

    def testFinishedGame_RandomTwoGame(self):
        testFinishedGame(self, '01273/X5/7/345400X70', 113)

    def testFinishedGame_RandomThreeGame(self):
        testFinishedGame(self, 'X7/90X088/06XXX81', 167)

    def testRooteGameFunction_PerfectGame(self):
        self.assertEqual(bowling.Game('XXXXXXXXXXXX').score, 300)


# test helper methods for games
class TestGameFunctions(unittest.TestCase):
    def testSpareBonuses(self):
        self.assertEqual(bowling.add_spare_bonus(['5']), 15)
        self.assertEqual(bowling.add_spare_bonus(['X']), 20)
        self.assertEqual(bowling.is_strike('X'), True)
        self.assertEqual(bowling.is_strike('7'), False)

    def testStrikeBonus(self):
        self.assertEqual(bowling.add_strike_bonus(['2', '7']), 19)
        self.assertEqual(bowling.add_strike_bonus(['X', '7']), 27)
        self.assertEqual(bowling.add_strike_bonus(['7', 'X']), 27)
        self.assertEqual(bowling.add_strike_bonus(['4', 'X']), 24)
        self.assertEqual(bowling.add_strike_bonus(['X', 'X']), 30)
        self.assertEqual(bowling.add_strike_bonus(['4', '/']), 20)

    def testIsStrike(self):
        self.assertEqual(bowling.is_strike('X'), True)
        self.assertEqual(bowling.is_strike('2'), False)
        self.assertEqual(bowling.is_strike('/'), False)
        self.assertEqual(bowling.is_spare('/'), True)
        self.assertEqual(bowling.is_spare('5'), False)

    def testResetPins(self):
        self.assertEqual(bowling.reset_pins(), 10)
        self.assertEqual(bowling.reset_pins('5'), 10)
        self.assertEqual(bowling.reset_pins('10'), 10)

    def testCheckValidThrow(self):
        self.assertEqual(bowling.check_valid_throw('3', 6), True)
        self.assertEqual(bowling.check_valid_throw('9', 9), True)
        self.assertEqual(bowling.check_valid_throw('7', 6), False)
        self.assertEqual(bowling.check_valid_throw('13', 10), False)
        self.assertEqual(bowling.check_valid_throw('8', 7), False)
        self.assertEqual(bowling.check_valid_throw('X', 7), False)
        self.assertEqual(bowling.check_valid_throw('B', 10), False)

    def testMisc(self):
        testUnfinishedGameWithStrings(self, '/9X8090XX9090x909090XX   ', 130)


# test unfinished game methods, once with raw inputs (limited scope: the input
# remains the same for the whole game, so each turn has the same score.) and
# once with strings (more options for different inputs)
class TestUnfinishedGameMethods(unittest.TestCase):
    "TestUnfinishedGameMethods tests new game, requires mock text inputs."
    def testMockInput_PerfectGame(self):
        testUnfinishedGameWithRawInputs(self, '10', 300)

    def testMockInput_Gutterballs(self):
        testUnfinishedGameWithRawInputs(self, '0', 0)

    def testMockInput_SinglePin(self):
        testUnfinishedGameWithRawInputs(self, '1', 20)

    def testMockInput_TwoPins(self):
        testUnfinishedGameWithRawInputs(self, '2', 40)

    def testMockInput_Spares(self):
        testUnfinishedGameWithRawInputs(self, '5', 150)

# testing score of unfinished ungame method - new uncompleted games,
# fed in one throw at a time. I adapted the calculate_unfinished_game()
# method to allow an input, which is not used when running the game normally.
    def testUnfinishedGame_PerfectGame(self):
        testUnfinishedGameWithStrings(self, 'XXXXXXXXXXXX   ', 300)

    def testUnfinishedGame_NoStrikesGame(self):
        testUnfinishedGameWithStrings(self, '90909090909090909090   ', 90)

    def testUnfinishedGame_SparesGame(self):
        testUnfinishedGameWithStrings(self, '5/5/5/5/5/5/5/5/5/5/5   ', 150)

    def testUnfinishedGame_RandomOneGame(self):
        testUnfinishedGameWithStrings(self, 'X7/729/XXX236/7/3   ', 168)

    def testUnfinishedGame_GutterballGame(self):
        testUnfinishedGameWithStrings(self, '00000000000000000000   ', 0)

    def testUnfinishedGame_RandomTwoGame(self):
        testUnfinishedGameWithStrings(self, '01273/X5/7/345400X70   ', 113)

    def testUnfinishedGame_RandomThreeGame(self):
        testUnfinishedGameWithStrings(self, 'X7/90X088/06XXX81   ', 167)

    def testTwoGames(self):
        testUnfinishedGameWithStrings(self, '/9X8090XX9090x909090yyyy   ', 130)


# if loading as main script
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(
        TestUnfinishedGameMethods)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
        TestGameFunctions))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
        TestFinishedGameMethods))
    unittest.TextTestRunner(verbosity=2).run(suite)
