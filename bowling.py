""" Maxwell Hunter - 8/24/18

Write a python module which implements a Game class that scores a game of bowling 
(see http://bowling.about.com/od/rulesofthegame/a/bowlingscoring.htm for a description of how bowling is scored).  

The class should provide two ways to calculate a bowling game score:

From an optional argument to the class initializer: a string between 12 and 21 characters long where each character represents a throw: X for a strike, 
/ for a spare, or a number indicating how many pins were knocked down.

Real time: The Game class should define a function that takes a single argument indicating the score of one throw, 
and returns the running score for the whole game.
The Game class should define a property which contains the calculated score of the game.

"""
import re #uses regular expressions on the calculate_unfinished_game() function

def add_spare_bonus(next_throw):
	bonus_score = 10 #Tracking a spare, we get 10 for the trame + the pins from the next thow.
	if next_throw[0] == "X": #if next throw is a strike, 
		bonus_score += 10 #then add 10
	else: #otherwise, add the next throw 
		bonus_score += int(next_throw[0]) #then add as a bonus
	return bonus_score #return the frame score for the spare + the bonus

def add_strike_bonus(next_two_throws): #calculates just the strike bonus, using the next two throws
	#by looking at the second to next throw first, we can deduce the total bonus easier
	bonus_score = 10 								#track bonus score, starting with the strike we got
	if next_two_throws[1].isdigit(): 				#if the second next throw is a number, ('X?#')
		bonus_score += int(next_two_throws[1]) 		#add that number to the frame score
		if next_two_throws[0] == "X":			 	#if first next throw is a strike ('XX#')
			bonus_score += 10 						#then add 10 again, the bonus from the second strike and a number from the third
		else: 										#the first next throw has to be a number if it's not a strike. ('X##')
			bonus_score += int(next_two_throws[0]) 	#so add it to the bonus
	elif next_two_throws[1] == "X": 				#if the second next throw is a strike ('X?X')
		bonus_score += 10			 				#then add 10 to the bonus and keep going
		if next_two_throws[0] == "X":			 	#if first next throw is also strike, ('Turkey')
			bonus_score += 10						#then add 10 again
		else:										#if first next throw is a number, ('XX?')
			bonus_score += int(next_two_throws[0]) 	#then add as a bonus
	elif next_two_throws[1] == "/":				 	#if second next throw is a spare, 
		bonus_score += 10							#add 10 and stop
	return bonus_score								#retun the total

def is_strike(char):
	if char == 'X':
		return True
	else:
		return False

def is_spare(char):
	if char == '/':
		return True
	else:
		return False

def print_scoreboard(frame_list, score_list, frame_idx, throw_number):
	for i in range(1,13):
		print "-",
	else: print
	print "|  SCOREMASTER 9000   |"
	for i in range(1,13):
		print "-",
	else: print
	for i in range(1,11):
		print " ----- ",
	else: print

	for i in range(1,11):
		if i == frame_idx+1:
			print "[ >{}<]".format(i),			#build the gameboard in a graphical display
		else:
			print "[  {}  ]".format(i),			#build the gameboard in a graphical display
	else: print

	for i in range(1,11):
		print " ----- ",
	else: print


	for i, frame in enumerate(frame_list): 		#for each frame in the game
		if i<frame_idx:							#if the frame has been played
			if i == 9:
				print '[{},{},{}]'.format(frame[0],frame[1],frame[2]), 

			elif sum(frame) == 10: 				#if the grame is totalled 10
				if frame[0] == 10: 				#if the first throw in the frame is 10, it's a strike
					print '[ X,- ]', 			#display a strike
				else: 							#if the first throw is not 10, it's a spare
					print '[{}, / ]'.format(frame[0]), #display a spare
			else: 								#if the frame total is not 10
				print '[ {},{} ]'.format(frame[0], frame[1]),

		elif i == frame_idx:
			if i == 9:
				if throw_number == 2: 				#if it's the third throw
					print '[{},{},*]'.format(frame[0],frame[1]), 
				elif throw_number == 1: 			#if it's the second throw
					print '[{},*, ]'.format(frame[0]), 
				else:
					print '[*, , ]',

			else:
				if throw_number == 1: 				#if it's the second throw
					print '[ {}, *]'.format(frame[0]), 
				else:
					print '[ *,  ]',

		elif i<9:
			print '[  ,  ]',
		elif i==9: 
			print '[ , , ]',
	print

	for i in range(0,10): 
		if i<frame_idx: 						#if the frame has been played
			running_total = sum(score_list[0:i+1])
			frame_string = str(running_total)
			if len(frame_string) == 3:
				print "[",frame_string,"]",
			elif len(frame_string) == 2:
				print "[ ",frame_string,"]",
			else:
				print "[ ",frame_string," ]",
		else:
			print "[     ]",
	else: print


	for i in range(1,11):
		print " ----- ",
	else: print;print

def calculate_finished_game(score_string):
	score = 0 									#track running score
	frame_idx = 0 								#track which frame we're on
	throw_number = 0 								#track which throw we're on
	is_bonus_throw = False						#track if there's an extra throw this frame
	score_string+='<<<' 						#add end characters, so the bonus doesn't loop and start from the first throw
	score_list = list(score_string) 			#convert the string to a list to make it easier to iterate
	frame_list = []
	for i in range(0,10):
		frame_list.append([0,0]) 						#create a list of each frame, and what they scored
	frame_list.append([0,0,0]) 					#add the special 10th frame
	score_list = [0]*12 				#create a list of the total scores for the frame

	for idx, throw in enumerate(score_string):
		if throw == '<':break							#if we encounter the end charactures, break the loop
		if frame_idx < 10:
			if throw.isdigit():
				if score_string[idx+1] == "/":			#if next throw is a spare, 
					frame_list[frame_idx][0]=int(throw)	#add the throw to the frame_list
				else: 									#if it's a normal throw,
					score_list[frame_idx] += int(throw) #just add to the frame score
					score += int(throw) 				#add to the running score also
					if not is_bonus_throw:
						throw_number+=1
						is_bonus_throw = True
					else:
						throw_number=0
						frame_idx+=1 					#move to the next frame
						is_bonus_throw = False

				frame_list[frame_idx][throw_number] = int(throw)

			elif is_strike(throw): 						#if the throw is a srike,
				strike_bonus = add_strike_bonus(score_string[idx+1:idx+3]) #calculte the strike using the next two throws as well
				score_list[frame_idx] += strike_bonus #add that value to the frame score
				frame_list[frame_idx][throw_number]=10
				score += strike_bonus 					#add that also to the strike bonus
				frame_idx+=1 							#move to the next frame
			elif is_spare(throw):
				spare_bonus = add_spare_bonus(score_string[idx+1:idx+2]) #set the score from the frame is 10 + whatever the next throw is, no matter what the first throw was (can only be a number (can't throw two spares in a row, or a spare after a strike))
				score_list[frame_idx] = spare_bonus #set that value to the frame score, it overrides any existing value
				frame_list[frame_idx][throw_number]=10-frame_list[frame_idx][0]
				score += spare_bonus					#add that also to the strike bonus
				frame_idx+=1 							#move to the next frame
	return score

def check_valid_throw(throw, pins):
	if not throw.isdigit(): 						#if input is a number (only numbers are accepted)
		return False
	if int(throw) > pins:					#check that the number isn't greater than the number of pins abailable
		print "no you didn't! there aren't that many pins left." 
		return False
	else: 
		return True

def reset_pins(pins=0):
	return 10

def calculate_unfinished_game():
	""" build a real-time function that takes user input as the game progresses. """
	#get user input
	print "No old game entered, starting new Game"
	score= frame_idx= throw_number= throw_idx= 0 				
												#track running score, which frame we're on, 
												# which throw we're on in the frame,
												# and the number of throws so far

												#throw_number checks which throw in the frame you're on,
												#throw_idx tracks the number of throws so far total.
	bonus_throw = False							#track if there's an extra throw this frame, only used in 10th frame
	throw_list = []								#create a list of throws as they come in
	frame_list = []
	for _ in range(0,9):
		frame_list.append([0,0])		 				#create a list of each frame, and what they scored - 
	#and add the first 9 frames
	frame_list.append([0,0,0]) 					#add the special 10th frame
	score_list = [0]*10 						#create a list of the total scores for the frame
	pins = reset_pins()							#track the number of pins standing
	throw_to_frame = {}							#track which throw goes to which frame

	while frame_idx<10: 						#while we're playing only 10 frames
		print;print 							#just to add two lines between throws
		print_scoreboard(frame_list, score_list, frame_idx, throw_number)
		print "You are on frame {} and are on your throw {}. Your running score is {}. There are {} pins standing.".format( #show 
			frame_idx+1, 						#show which frame 
			throw_number+1, 					#and throw they're on
			sum(score_list), 					#and their score
			pins, 								#and how many pins are standing
			)
		print;print 							#just to add two lines between throws

		#calculate user input
		throw = raw_input("After your throw, enter a number 0-10. > ") #get user input

		if str(throw) in ["x","X"]:				#convert X to strike
			throw="10"
		if str(throw) == "/":					#convert / to spare
			if throw_number:
				throw=str(10-throw_list[throw_idx-1])
			else:
				print "Cannot get spare on first throw!"
				throw="100"						#throws an error, try again (no pun intended)


		if not check_valid_throw(throw,pins):	#check that the number isn't greater than the number of pins abailable
			print "Enter only numbers, please."
			continue 							#if it's invalid, try again
		throw = int(throw)						#cast to int
		throw_list.append(throw)				#save throw in throw_list
		throw_to_frame[str(throw_idx)]=frame_idx #save which throw was in which frame
		frame_list[frame_idx][throw_number]=throw #save throw score into the throw score sheet
		score_list[frame_idx]+=throw 			#save throw into the frame score sheet
		pins-=throw 							#update how many pins are standing after the throw

		#check for strikes and spares
		if len(throw_list)>1: 						#if we can check last throw
			if throw_list[throw_idx-1] == 10: 		#if last throw was a strike
				if throw_to_frame[str(throw_idx-1)]<9: #if last frame was in the first 9
					score_list[throw_to_frame[str(throw_idx-1)]]+=throw #add this throw to the frame for that throw
			elif throw_number<1:
				if score_list[frame_idx-1] == 10: 	#if last frame was a spare
					score_list[frame_idx-1] += throw #add this throw to last frame
		if len(throw_list)>2: 						#if we can check two throws ago
			if throw_list[throw_idx-2] == 10: 		#if second to last throw was a strike
				if throw_to_frame[str(throw_idx-2)]<9: #if second to last frame was in the first 9 
					score_list[throw_to_frame[str(throw_idx-2)]]+=throw #add this throw to the score from that frame


		#what to do after the throw depends on several factors
		if frame_idx<9: 							#first nine frames
			if throw_number < 1: 					#first throw
				if pins > 0: 						#if there are pins left
					throw_number+=1 				#go to second throw in frame
				else: 								#if there are no pins left
					print "Strike!";print
					pins = reset_pins(pins) 		#reset pins
					frame_idx=move_to_next_frame(frame_idx) #go to next frame
					throw_number=0
			else: 									#second throw
				if pins == 0: 						#if there are pins left
					print "Spare!";print
				frame_idx+=1 						#go to next frame
				throw_number=0						#reset throw_number to 0
				pins = reset_pins(pins) 			#reset pins

		else: 										# final 10th frame
			if throw_number < 1: 					#first throw
				if pins == 0: 						#if there no are pins left
					print "Strike!";print
					pins = reset_pins(pins) 		#reset pins
					bonus_throw=True 				#you get a bonus 3rd throw
			elif throw_number < 2: 					#second throw
				if pins == 0: 						#if there no are pins left
					if throw_list[throw_idx-1]==10:	#if last throw was a strike,
						print "Strike!";print 		
					else:	 						#if last throw was not a strike,
						print "Spare!";print
					bonus_throw=True 				#either way, you get a bonus 3rd throw
				pins = reset_pins(pins) 			#reset pins
				if not bonus_throw:					#if you don't have a bonus throw
					frame_idx+=1 					#go to next frame, ends the game
			elif throw_number < 3: 					#third throw
													#Done! nothing special happens.
				frame_idx+=1						#go to next frame, ends the game
			throw_number+=1							#increment throw_number
		throw_idx+=1								#increment throw_idx

	print_scoreboard(frame_list, score_list, frame_idx, throw_number)
	_ = raw_input("Game Over!")
	print;print
	print "final score: {}".format(sum(score_list))
	if raw_input("Play again? Enter 'Y', or press enter to quit. ").lower()=='y':
		Game()

class Game(object):
	score=0
	score_string=""
	def __init__(self, score_string=""):
		"""docstring for Game

		#Class should provide two ways to calculate a bowling game score:
		1. From an optional argument to the class initializer: {completed}
		2. Real time: The Game class should define a function that takes 
		a single argument indicating the score of one throw, 
		and returns the running score for the whole game.
		"""

		if score_string: 										#if an argument was entered, 
		 	self.score = calculate_finished_game(score_string) 	#calculate using the finished game method
	 	else: 													#if an argument was nor entered, 
	 		self.score = calculate_unfinished_game() 			#calculate using the unfinished game method (collects user input)

#test assertions
assert Game('XXXXXXXXXXXX').score == 300
assert Game('90909090909090909090').score == 90
assert Game('5/5/5/5/5/5/5/5/5/5/5').score == 150
assert Game('X7/729/XXX236/7/3').score == 168
assert Game('00000000000000000000').score == 0
assert Game('01273/X5/7/345400X70').score == 113
assert Game('X7/90X088/06XXX81').score == 167

print 'Assertions passed! you did it!'

Game()
