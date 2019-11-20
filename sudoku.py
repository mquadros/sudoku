import random
import sys

### Generate and print a valid sudoku board
class Sudoku():
	def __init__(self):
		#Generate Sodoku board, an array of numbers
		self.board = []
		#Base for the sudoku puzzle (default is 3 for a standard 9x9 board)
		#2 also works, but larger than three is exponentially longer to calculate
		self.base = 3
		self.square = self.base * self.base
		length = self.base * self.base
		#Valid numbers to use (1 through 9 for a standard 9x9 board)
		self.numbers = range(length +1 )[1:length+1]
		self.row_length = length
		self.col_length = self.row_length
		#Boolean for whether the board is valid or an error is detected
		self.error = False
		#group describes which square the number is in
		group = 1
		i = 1
		#loop through the full board creating number objects
		for r in range(self.row_length):
			for c in range(self.col_length):
				# create a new number object
				x = Number()
				# row and col are positional values for the number on the board
				x.row = r+1
				x.col = c+1
				# set the group number
				x.set_group(self.base)
				i+=1
				# set the value
				x.set_val(self.board,length)
				# if there is no valid value for the number, the board is not valid
				if x.value =="E":
					self.error = True
				self.board.append(x)

	# print out an ascii sudoku board
	def printboard(self):
		i = 0
		#Print one row at a time
		for r in range(self.row_length):
			#loop through each group
			for m in range(self.base):
				#loop through each row of each group
				for p in range(self.base):
					# calculate which column position we are at
					c = p+(self.base*m)+1
					#loop through all number objects in the board
					for num in self.board:
						#print number that matches position values
						#not the most efficient way to print the board, but it works and I don't care
						if r+1 == num.row and c == num.col:
							sys.stdout.write("{0}".format(num.value))
				#print a vertical divider between groups
				if m != self.base-1:
					sys.stdout.write(" | ")
			#Print a horizontal divider between groups
			#Logic: if the row we are on is the last before the next group (which has length equal to base), and we aren't on the last row, print the divider
			if r%self.base == self.base-1 and r != self.row_length-1:
				print("")
				sys.stdout.write("{0}".format("-"*(self.square + (3 * (self.base -1)))))
			#Print a new line at the end of each row except the last row
			if r!= self.col_length-1:
				print("")

class Number():
	def __init__(self):
		#is the number valid
		self.valid = False
		self.value = 0
		#which grouping is the piece in. Values are 1 through 9
		self.group = 0
		self.row = 0
		self.col = 0

	def set_group(self,base):
		# Groups works like such:
		# 111 | 222 | 333
		# 111 | 222 | 333
		# 111 | 222 | 333
		# ---------------
		# 444 | 555 | 666
		# 444 | 555 | 666
		# 444 | 555 | 666
		# ---------------
		# 777 | 888 | 999
		# 777 | 888 | 999
		# 777 | 888 | 999
		#taking advantage of ints truncating values - divide the column (minus one) by base and add 1, divide row (minus one) by base but add that as a multiple of the base (similar to doing non base 10 math!)
		#Ex. Base 3, position [row 4, column 8] Group 6 - column-1 divided by base is 2.3, truncated to 2, plus 1 is 3. Row-1 divided by base is 1, times base is 3. 3+3 is 6, the proper group.
		g = (int((self.col-1) / base + 1))+((int((self.row-1)/base))*base)
		self.group = g

	def set_val(self,board,length):
		#Initialize with a random value
		self.value = random.randint(1,length)
		#i is used to see if we've looped through every valid number
		i = 0
		#keep looping until we find a valid number or conclude no valid number exists
		while self.valid == False and self.value != "E":
			#tracker to see if the number is valid
			t = True
			#if this is the first number, any number is valid
			if board == []:
				self.valid = True
			else:
				#loop through every number in the board
				for num in board:
					#if a number in the same row has that value, the number is invalid
					if num.row == self.row and num.value == self.value:
						t = False
					#if there is a matching value in the column, the number is invalid
					if num.col == self.col and num.value == self.value:
						t = False
					#if the value already exists in the group, the number is invalid
					if num.group == self.group and num.value == self.value:
						t = False
			#if the number is invalid and we haven't looped through all the numbers, increment the value by 1 and try again
			if t == False and i < length:
				self.value += 1
				#if the number is greater than the max number, loop back to 1.
				if self.value > length:
					self.value =1
			if i == length:
				#set valid to true to break loop, set value to E to signal board is invalid
				self.valid = True
				self.value = "E"
			i +=1
			self.valid = t

#i tracks how many boards were tested
i = 1
status = True
while status == True:
	#create new boards until a valid board is found, and the creation status is no longer true
	x = Sudoku()
	status = x.error
	if status == True:
		# print a star for each attempt
		sys.stdout.write("{0}".format("*"))
	i += 1
print("")
print("Board found on attempt " + str(i))
#print the board
x.printboard()

