class BinaryTree (object):
	def __init__ (self, node):
		self.node = node
		self.left = left
		self.right = right

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
