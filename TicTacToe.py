import random
import copy

class ticTacToe:
	def __init__(self):
		super().__init__()
		self.placed = list(range(0,9))
		self.turn = ""
		self.movesLeft = list(range(0,9))
		self.outcome = ""

	def setTurn(self, turn):
		self.turn = turn
	
	def getOutcome(self):
		return self.outcome

	def displayBoard(self):
		print("\n%s|%s|%s" %(str(self.placed[0]), str(self.placed[1]), str(self.placed[2])))
		print("-+-+-")
		print("%s|%s|%s" %(str(self.placed[3]), str(self.placed[4]), str(self.placed[5])))
		print("-+-+-")
		print("%s|%s|%s\n" %(str(self.placed[6]), str(self.placed[7]), str(self.placed[8])))

	def checkWin(self):
		for i in range(0, 9, 3):
			if(self.placed[i] == self.placed[i+1] == self.placed[i+2]):
				self.outcome = self.turn
				return True
		for i in range(0, 3):
			if(self.placed[i] == self.placed[i+3] == self.placed[i+6]):
				self.outcome = self.turn
				return True
		if(self.placed[0] == self.placed[4] == self.placed[8]):
			self.outcome = self.turn
			return True
		if(self.placed[2] == self.placed[4] == self.placed[6]):
			self.outcome = self.turn
			return True
		if (len(self.movesLeft) == 0):
			self.outcome = "T"
			return True # resulted in a Tie
		return False

	def getValidMoves(self):
		return self.movesLeft
		
	def setValidMoves(self, validMoves):
		self.movesLeft = validMoves
		return 

	def validMoves(self):
		movesList = []
		for i in range(len(self.placed)):
			if (isinstance(self.placed[i], int)):
				movesList.append(i)
		self.movesLeft = movesList
		return movesList
	
	def chooseMove(self,result=None):
		movesList = self.movesLeft
		valid = False
		while (not valid):
			if (result not in movesList):
				print("Not a valid tile\n")
			else:
				self.placeMove(result)
				movesList = self.validMoves()
				valid = True
		return
	
	def placeMove(self, result):
		self.placed[int(result)] = self.turn


class MCTS:
	def __init__(self, origGame):
		super().__init__()
		self.origGame = origGame
	
	def findMoves(self): 
		chosenMove = 0
		initValidMoves = self.origGame.getValidMoves()
		moveWins = {}
		for move in initValidMoves:
			moveWins[move] = 0

		for move in initValidMoves:
			for i in range(1000): # Number of playout computer does
				moveWins[move] += self.playGame(move)
		chosenMove = max(moveWins, key=moveWins.get)
		return chosenMove


	def playGame(self, move):
		result = False
		game = copy.deepcopy(self.origGame)
		game.chooseMove(move)
		result = game.checkWin()
		game.setTurn("X") if game.turn == "O" else game.setTurn("O")
		while(not result and len(game.movesLeft) != 0): # condition included for computer going first
			randTile = random.choice(game.movesLeft)
			game.chooseMove(randTile)
			result = game.checkWin()
			if (result):
				break
			game.setTurn("X") if game.turn == "O" else game.setTurn("O")
		if (game.getOutcome() == "X"):
			return -1 # Loss
		elif (game.getOutcome() == "O"):
			return 1 # win
		else:
			return 0 # Tie 

def playerInput(movesList):
	valid = False
	while(not valid):
		move = input("Choose a tile: ")
		try:
			tile = int(move)
			if (tile in movesList):
				valid = True
		except:
			print("Not a valid tile\n")
	return tile

def play_a_new_game():
	game = ticTacToe()
	ai = MCTS(game)
	result = False
	firstPlayer = input("Who goes first, Player(X) or Computer(O)? ") # decide whose turn
	if (firstPlayer == "X" or firstPlayer == "x"):
		game.setTurn("X")
	else:
		game.setTurn("O")
	while(not result):
		game.displayBoard()
		if(game.turn == "X"):
			move = playerInput(game.movesLeft)
			game.chooseMove(move)
		else:
			move = ai.findMoves()
			game.chooseMove(move)
			print("Computer chose: " + str(move))
		result = game.checkWin()
		if (result):
			break
		game.setTurn("X") if game.turn == "O" else game.setTurn("O")
	game.displayBoard()
	outcome = game.getOutcome()
	if (outcome == "T"):
		print("It's a tie")
	else:
		print(game.getOutcome() + " wins!")
	print("Game finished")
	
if __name__ == "__main__":
	play_a_new_game()
