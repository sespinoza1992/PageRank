#!/usr/bin/python
from node import Node

class Graph:
	def __init__(self):
		self.nodes = {}

	def getNode(self, id):
		if id not in self.nodes:
			self.nodes[id] = Node(id)
		return self.nodes[id]

	###
	#	Adds an edge from one node
	#	to another node
	###
	def addEdge(self, fromID, toID, weight = 1):
		fromNode = self.getNode(fromID)
		toNode = self.getNode(toID)

		fromNode.addOut(toNode, weight)
		toNode.addIn(fromNode, weight)

	def sort(self):
		values = self.nodes.values()
		values.sort()
		return values
		
	###
	#	Iterates over the graph's nodes
	###
	def __iter__(self):
		return self.nodes.itervalues()

	###
	#	Returns the number of nodes in
	#	the graph
	###
	def __len__(self):
		return len(self.nodes)