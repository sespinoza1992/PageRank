#!/usr/bin/python

class Node:
	def __init__(self, id):
		self.ins = {}
		self.outs = {}
		self.id = id
		self.oldRank = 0
		self.newRank = 0
		self.contribution = -1

	###
	#	Adds an outbound edge
	#	from a node
	###
	def addOut(self, toNode, weight):
		self.outs[toNode] = weight

	###
	#	Adds an inbound edge
	#	from a node
	###
	def addIn(self, fromNode, weight):
		self.ins[fromNode] = weight

	###
	#	Iterates over this
	#	node's inbound edges
	###
	def __iter__(self):
		return self.ins.iteritems()

	###
	#	Returns the number
	#	of outbound edges
	###
	def __len__(self):
		return len(self.outs)

	###
	#	Returns a hashed representation
	#	of this node
	###
	def __hash__(self):
		return hash(self.id)

	###
	#
	###
	def __eq__(self, other):
		return self.id == other.id

	def __str__(self):
		return str(self.id)

	def __repr__(self):
		return str(self)

	def __cmp__(self, other):
		return cmp(other.newRank, self.newRank)