import unittest
import bowling

class TestGameMethods(unittest.TestCase):
	#testing score of finished game method - new completed games
    def testPerfectGame(self):
		self.assertEqual(bowling.Game('XXXXXXXXXXXX').score,300)
    def testNoStrikesGame(self):
		self.assertEqual(bowling.Game('90909090909090909090').score,90)
    def testSparesGame(self):
		self.assertEqual(bowling.Game('5/5/5/5/5/5/5/5/5/5/5').score,150)
    def testRandomOneGame(self):
		self.assertEqual(bowling.Game('X7/729/XXX236/7/3').score,168)
    def testGutterballGame(self):
		self.assertEqual(bowling.Game('00000000000000000000').score,0)
    def testRandomTwoGame(self):
		self.assertEqual(bowling.Game('01273/X5/7/345400X70').score,113)
    def testRandomThreeGame(self):
		self.assertEqual(bowling.Game('X7/90X088/06XXX81').score,167)

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


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestGameMethods)

	unittest.TextTestRunner(verbosity=2).run(suite)
