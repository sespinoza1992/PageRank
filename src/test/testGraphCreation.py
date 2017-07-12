#!/usr/bin/python
import sys
sys.path.append('../lib/graph')

from graph import Graph
from node import Node

graph = Graph()

graph.addEdge('joel', 'sal')

print graph.getNode('joel').ins
print graph.getNode('joel').outs

for n in graph.getNode('joel').ins:
	print n

for n in graph.getNode('joel').outs:
	print n