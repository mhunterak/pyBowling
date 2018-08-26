import unittest
import bowling

class TestGameMethods(unittest.TestCase):
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

if __name__ == '__main__':
	unittest.main()
