#!/usr/bin/python
import sys
sys.path.append('../lib/pagerank')
sys.path.append('../lib/graph')
sys.path.append('../lib')

import re
from graph import Graph
from rank import pageRank

graph = Graph()

with open('test.txt', 'r') as f:
	
	skipComments = (line for line in f if line[0] != '#')
	edges = (re.split("\s+", edge) for edge in skipComments)
	for edge in edges:
		graph.addEdge(edge[0], edge[1])

print "Ranking starting..."

time, results = pageRank(0.0001, 0.85, graph)

print "Iterations:", results.iterationNumber()
print "Page Rank Time:", time, "seconds"
print "Items:"
for item in results.sorted():
	node, rank = item
	print (node, rank, len(node.ins))
