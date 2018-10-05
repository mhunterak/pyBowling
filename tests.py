import unittest
import bowling

class TestFinishedGameMethods(unittest.TestCase):
	#testing score of finished game method - new completed games
	def testPerfectGame(self):
		self.assertEqual(bowling.calculate_finished_game('XXXXXXXXXXXX'),300)

	def testNoStrikesGame(self):
		self.assertEqual(bowling.calculate_finished_game('90909090909090909090'),90)

	def testSparesGame(self):
		self.assertEqual(bowling.calculate_finished_game('5/5/5/5/5/5/5/5/5/5/5'),150)

	def testRandomOneGame(self):
		self.assertEqual(bowling.calculate_finished_game('X7/729/XXX236/7/3'),168)

	def testGutterballGame(self):
		self.assertEqual(bowling.calculate_finished_game('00000000000000000000'),0)

	def testRandomTwoGame(self):
		self.assertEqual(bowling.calculate_finished_game('01273/X5/7/345400X70'),113)

	def testRandomThreeGame(self):
		self.assertEqual(bowling.calculate_finished_game('X7/90X088/06XXX81'),167)

	def testSpareBonuses(self):
		self.assertEqual(bowling.add_spare_bonus(['5']),15)
		self.assertEqual(bowling.add_spare_bonus(['X']),20)
		self.assertEqual(bowling.is_strike('X'), True)

	def testStrikeBonus(self):
		self.assertEqual(bowling.add_strike_bonus(['2','7']),19)
		self.assertEqual(bowling.add_strike_bonus(['X','7']),27)
		self.assertEqual(bowling.add_strike_bonus(['4','X']),24)
		self.assertEqual(bowling.add_strike_bonus(['X','X']),30)
		self.assertEqual(bowling.add_strike_bonus(['4','/']),20)

	def testIsStrike(self):
		self.assertEqual(bowling.is_strike('X'), True)
		self.assertEqual(bowling.is_strike('2'), False)
		self.assertEqual(bowling.is_strike('/'), False)
		self.assertEqual(bowling.is_spare('/'), True)
		self.assertEqual(bowling.is_spare('5'), False)

	def testResetPins(self):
		self.assertEqual(bowling.reset_pins(), 10)
		self.assertEqual(bowling.reset_pins('5'), 10)

class TestUnfinishedGameMethods(unittest.TestCase):
	"""TestUnfinishedGameMethods tests new game, which requires mock text inputs. 
	At this time, I've only set the raw_input value once, and it stays
	the same input through the whole game. """
	def test_mock_input_perfect_game(self):
		original_raw_input = __builtins__.raw_input
		__builtins__.raw_input = lambda _: '10'
		self.assertEqual(bowling.calculate_unfinished_game(), 300)
		__builtins__.raw_input = original_raw_input

	def test_mock_input_gutterballs(self):
		original_raw_input = __builtins__.raw_input
		__builtins__.raw_input = lambda _: '0'
		self.assertEqual(bowling.calculate_unfinished_game(), 0)
		__builtins__.raw_input = original_raw_input

	def test_mock_input_single_pin(self):
		original_raw_input = __builtins__.raw_input
		__builtins__.raw_input = lambda _: '1'
		self.assertEqual(bowling.calculate_unfinished_game(), 20)
		__builtins__.raw_input = original_raw_input

	def test_mock_input_two_pins(self):
		__builtins__.raw_input = lambda _: '2'
		self.assertEqual(bowling.calculate_unfinished_game(), 40)

	def test_mock_input_spares(self):
		original_raw_input = __builtins__.raw_input
		__builtins__.raw_input = lambda _: '5'
		self.assertEqual(bowling.calculate_unfinished_game(), 150)
		__builtins__.raw_input = original_raw_input


	#testing score of finished ungame method - new uncompleted games, 
	#fed in one throw at a time
	def testPerfectGame(self):
		self.assertEqual(bowling.calculate_unfinished_game('XXXXXXXXXXXX   '),300)

	def testNoStrikesGame(self):
		self.assertEqual(bowling.calculate_unfinished_game('90909090909090909090   '),90)

	def testSparesGame(self):
		self.assertEqual(bowling.calculate_unfinished_game('5/5/5/5/5/5/5/5/5/5/5   '),150)

	def testRandomOneGame(self):
		self.assertEqual(bowling.calculate_unfinished_game('X7/729/XXX236/7/3   '),168)

	def testGutterballGame(self):
		self.assertEqual(bowling.calculate_unfinished_game('00000000000000000000   '),0)

	def testRandomTwoGame(self):
		self.assertEqual(bowling.calculate_unfinished_game('01273/X5/7/345400X70   '),113)

	def testRandomThreeGame(self):
		self.assertEqual(bowling.calculate_unfinished_game('X7/90X088/06XXX81   '),167)



if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestUnfinishedGameMethods)
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFinishedGameMethods))
	#mock input tests require more screen real estate, so we're gonna run those first
	unittest.TextTestRunner(verbosity=3).run(suite)
