#!/usr/bin/python


from decorate import memoize
from decorate import memoize_t
from decorate import clear_t
from decorate import timeme

import operator


@memoize
def invLen(thing):
	return 1.0 / len(thing)

@memoize
def randPart(graph, clickProb):
	return (1 - clickProb) * invLen(graph)

def contribution(node):
	return invLen(node) * node.oldRank

def converged(epsilon, graph):
	diffs = (node.newRank - node.oldRank for node in graph)
	areLess = (val < epsilon for val in diffs)
	return all(areLess)

def firstIteration(graph):
	for node in graph:
		node.oldRank = invLen(graph)

def nextIteration(graph, clickProb):
	for node in graph:
		s = 0
		for inNode, edgeWeight in node:
			if inNode.contribution == -1:
				inNode.contribution = contribution(inNode)
			s += inNode.contribution * edgeWeight
		node.newRank = randPart(graph, clickProb) + s

def moveNext(graph):
	for node in graph:
		node.oldRank = node.newRank
		node.contribution = -1

@timeme
def pageRank(epsilon, clickProb, graph):
	firstIteration(graph)
	nextIteration(graph, clickProb)
	i = 1
	while not converged(epsilon, graph):
		moveNext(graph)
		nextIteration(graph, clickProb)
		i += 1
		#print i

	return (graph.sort(), i)