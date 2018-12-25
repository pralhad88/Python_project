theboard = {
			"top-l": ' ', 'top-m':' ','top-r':' ',
			"mid-l": ' ', 'mid-m':' ','mid-r':' ', 
			"low-l": ' ', 'low-m':' ','low-r':' ' 
			} # Dictionary indicates the board of game.
print()
print('* WELCOME TO THE Tic_Toc_Toe GAME *'.center(100,))
print()
print('''Instruction:- If computer ask you, "Enter your move" then you have enter following line as your conviniance. 
	1. If you like to fill your mark on a top of the board then enter, top-l, top-m or top-r.
	2. If you want to fill your mark on a middel of the board then enter, mid-l, mid-m, or mid-r.
	3. If you want to fill your mark on a bottom of the board then enter, low-l, low-m or low-r.
	4. The '-l' means left side of the board, '-m' means middel of the board and '-r' means right side of the board.
	5. Let's play the game ''')
print()

player1 = input("Enter frist player name ")
player2 = input("Enter second player name ")
player = player1

def Board(theboard): # function shows the status of board
	print()
	print(theboard['top-l'] + '|' + theboard['top-m'] + '|' + theboard['top-r'])
	print('-+-+-')
	print(theboard['mid-l'] + '|' + theboard['mid-m'] + '|' + theboard['mid-r'])
	print('-+-+-')
	print(theboard['low-l'] + '|' + theboard['low-m'] + '|' + theboard['low-r'])
	
turn = 'x'
while True:
	for i in range(9): # loop used for our markeble input
		Board(theboard)
		print()
		print("Which place wloud you like to fill " + turn + '. ' + player)
		print()
		move = input("Enter your move ")
		theboard[move] = turn
		
		if turn == 'x': # there are eight condition to check wheather player win the game or not for both of the player.
			turn = 'o'
			player = player2
			if (theboard['top-l'] == theboard['top-m'] and theboard['top-l'] != ' ') and  (theboard['top-m'] == theboard['top-r']):
				Board(theboard)
				print(player1 + ' you have won the game')
				break
			elif (theboard['mid-l'] == theboard['mid-m'] and theboard['mid-l'] != ' ') and  (theboard['mid-m'] == theboard['mid-r']):
				Board(theboard)
				print(player1 + ' you have won the game')
				break
			elif (theboard['low-l'] == theboard['low-m'] and theboard['low-l'] != ' ') and  (theboard['low-m'] == theboard['low-r']):
				Board(theboard)
				print(player1 + ' you have won the game')
				break
			elif (theboard['top-l'] == theboard['mid-l'] and theboard['top-l'] != ' ') and  (theboard['mid-l'] == theboard['low-l']):
				Board(theboard)
				print(player1 + ' you have won the game')
				break
			elif (theboard['top-m'] == theboard['mid-m'] and theboard['top-m'] != ' ') and  (theboard['mid-m'] == theboard['low-m']):
				Board(theboard)
				print(player1 + ' you have won the game')
				break
			elif (theboard['top-r'] == theboard['mid-r'] and theboard['top-r'] != ' ') and  (theboard['mid-r'] == theboard['low-r']):
				Board(theboard)
				print(player1 + ' you have won the game')
				break
			elif (theboard['top-l'] == theboard['mid-m'] and theboard['top-l'] != ' ') and  (theboard['mid-m'] == theboard['low-r']):
				Board(theboard)
				print(player1 + ' you have won the game')
				break
			elif (theboard['top-r'] == theboard['mid-m'] and theboard['top-r'] != ' ') and  (theboard['mid-m'] == theboard['low-l']):
				Board(theboard)
				print(player1 + ' you have won the game')
				break

		else:
			turn = 'x'
			player = player1
			if (theboard['top-l'] == theboard['top-m'] and theboard['top-l'] != ' ') and  (theboard['top-m'] == theboard['top-r']):
				Board(theboard)
				print(player2 + ' you have won the game')
				break
			elif (theboard['mid-l'] == theboard['mid-m'] and theboard['mid-l'] != ' ') and  (theboard['mid-m'] == theboard['mid-r']):
				Board(theboard)
				print(player2 + ' you have won the game')
				break
			elif (theboard['low-l'] == theboard['low-m'] and theboard['low-l'] != ' ') and  (theboard['low-m'] == theboard['low-r']):
				Board(theboard)
				print(player2 + ' you have won the game')
				break
			elif (theboard['top-l'] == theboard['mid-l'] and theboard['top-l'] != ' ') and  (theboard['mid-l'] == theboard['low-l']):
				Board(theboard)
				print(player2 + ' you have won the game')
				break
			elif (theboard['top-m'] == theboard['mid-m'] and theboard['top-m'] != ' ') and  (theboard['mid-m'] == theboard['low-m']):
				Board(theboard)
				print(player2 + ' you have won the game')
				break
			elif (theboard['top-r'] == theboard['mid-r'] and theboard['top-r'] != ' ') and  (theboard['mid-r'] == theboard['low-r']):
				Board(theboard)
				print(player2 + ' you have won the game')
				break
			elif (theboard['top-l'] == theboard['mid-m'] and theboard['top-l'] != ' ') and  (theboard['mid-m'] == theboard['low-r']):
				Board(theboard)
				print(player2 + ' you have won the game')
				break
			elif (theboard['top-r'] == theboard['mid-m'] and theboard['top-r'] != ' ') and  (theboard['mid-m'] == theboard['low-l']):
				Board(theboard)
				print(player2 + ' you have won the game')
				break

		if i == 8: # If above condition are not satisfied then it say's that match is draw
			print("Match is draw ! ")
	
	for j in theboard.keys(): # This loop used if player wnat to play again then it will erase the value of dictionary and added the one empty string.
		theboard[j] = ' '

	playagain = input('Hey guys Would you like to play again ? if yes then press "yes" ') 
	
	if playagain == 'yes':
		continue
	
	else:
		break