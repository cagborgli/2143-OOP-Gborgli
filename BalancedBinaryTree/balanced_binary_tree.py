#Christopher Gborgli
#Abdullah Alathel
import random
import time

class BalancedSearch(object):
	def __init__(self,size=16):
		self.tree = [-1 for x in range(size)]
		self.size = size
		self.root = 1
		self.items = 0
		self.values_array = []

#@Name:
#	LoadT
#@Description:
#	Receives a list of values then call the "order" function with that list then pass values to the function "insert"
#@Params:
#	a list
#@Returns:
#	None

	def LoadT(self,_array):
		self.order(_array)
		for v in self.values_array:
			self.insert(v)

#@Name:
#	insert
#@Description:
#	Receives values and put them in the correct tree index
#@Params:
#	a value
#@Returns:
#	None

	def insert(self,val):
		# If list (tree) is empty, put value at root
		if self.tree[self.root] == -1:
			self.tree[self.root] = val
		# loop until you find the location to insert
		# even if you have to extend this list
		else:
			i = self.root
			loop = True
			while loop:
				if val > self.tree[i]:
					i = self.rightChild(i)
				else:
					i = self.leftChild(i)

				if i >= self.size:
					self.extend()

				if self.tree[i] == -1:
					self.tree[i] = val
					self.items += 1
					loop = False

#@Name:
#	order
#@Description:
#	Receives a list of values and sort them according to the binary tree representation in a new list
#@Params:
#	a list
#@Returns:
#	None

	def order(self,_Array):

		if len(_Array) == 3:
			self.values_array.append(_Array[1])
			self.values_array.append(_Array[0])
			self.values_array.append(_Array[2])
			return
		else:
			mid = len(_Array)//2
			RTlist = _Array[mid+1:]
			LTlist = _Array[:mid]
			if _Array[mid] not in self.values_array:
				self.values_array.append(_Array[mid])
			self.order(LTlist)
			self.order(RTlist)

#@Name:
#	extend
#@Description:
#	 extends the length of the tree list by 2 and prints the number of items
#@Params:
#	None
#@Returns:
#	None

	def extend(self):
		temp = [-1 for x in range(self.size)]
		self.tree.extend(temp)
		self.size *= 2
		print(self.items)

#@Name:
#	find
#@Description:
#	  Find if a value exists in the tree and how many comparisons it took to find it
#@Params:
#	value to be seached for
#@Returns:
#	None

	def find(self,key):

		self.comparisons = 1

		if key == self.tree[self.root]:
			return True
		else:
			i = self.root
			while True:
				if key < self.tree[i]:
					i = self.leftChild(i)
				else:
					i = self.rightChild(i)

				if i >= self.size:
					return False

				if self.tree[i] == -1:
					return False

				if self.tree[i] == key:
					return True

				self.comparisons += 1

#@Name:
#	leftChild
#@Description:
#	  Determines the position of the left child given the root
#@Params:
#	integer
#@Returns:
#	integer

	def leftChild(self,i):
		return 2 * i

#@Name:
#	rightChild
#@Description:
#	  Determines the position of the right child given the root
#@Params:
#	integer
#Returns:
#	integer

	def rightChild(self,i):
		return 2 * i + 1
	def p (self):
		print(self.tree)

random.seed(time.time())
num = input("How many values would you like to put in the tree ?")
num = int(num)
if num > 1:
	bs = BalancedSearch(num)
	unique = []
# loop 1000 times
	for x in range(num-1):
# get a random number
		r = random.randint(0,999999)
# if it's not already in the list, enter it.
		if r not in unique:
			unique.append(r)
	unique.sort()
	bs.LoadT(unique)
	bs.p()
else:
	bt = BalancedSearch()
	unique = []
# loop 1000 times
	for x in range(15):
# get a random number
		r = random.randint(0,999999)
# if it's not already in the list, enter it.
		if r not in unique:
			unique.append(r)
	unique.sort()
	bt.LoadT(unique)
	bt.p()
