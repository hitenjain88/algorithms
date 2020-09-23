class BinaryTree (object):
	def __init__ (self, node):
		self.node = node
		self.left = None
		self.right = None

	def addChild (self, childNode):
		if childNode == self.node:
			return

		# Go to the left
		elif childNode < self.node:
			if self.left:
				self.left.addChild (childNode)			
			else:
				self.left = BinaryTree (childNode)

		# Go to the right
		else:
			if self.right:
				self.right.addChild (childNode)
			else:
				self.right = BinaryTree (childNode)

	def sortTree (self):
		array = []

		if self.left:
			array += self.left.sortTree ()

		array.append (self.node)

		if self.right:
			array += self.right.sortTree ()

		return array		

def buildTree (array):
	root = BinaryTree (array[0])

	for idx in range (1, len(array)):
		root.addChild(array[idx])

	return root

def main ():
	array = [5,4,7,2,11,14,6]

	tree = buildTree (array)

	sortedArray = tree.sortTree()
	
	print (array)
	print (sortedArray)

main()
