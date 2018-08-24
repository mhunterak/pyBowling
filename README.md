# pyBowling
Python based bowling scoring machine

based on a pre-employment code challenge

(see http://bowling.about.com/od/rulesofthegame/a/bowlingscoring.htm for a description of how bowling is scored).  

The class should provide two ways to calculate a bowling game score:

From an optional argument to the class initializer: a string between 12 and 21 characters long where each character represents a throw: X for a strike, 
/ for a spare, or a number indicating how many pins were knocked down.

Real time: The Game class should define a function that takes a single argument indicating the score of one throw, 
and returns the running score for the whole game.
The Game class should define a property which contains the calculated score of the game.
