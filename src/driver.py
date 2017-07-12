#!/usr/bin/python
import sys
import os
__dir__ = os.path.dirname(os.path.realpath(__file__))
sys.path.append(__dir__ + '/lib/pagerank')
sys.path.append(__dir__ + '/lib/graph')
sys.path.append(__dir__ + '/lib/parse')
sys.path.append(__dir__ + '/lib')
import math
import argparse

from itertools import izip


from rank import pageRank
from parse import parsefour, parsefootball, parseSNAP, parsebasketball
from graph import Graph
from decorate import timeme


parsers = {
	'four': parsefour,
	'football': parsefootball,
	'snap': parseSNAP,
   'bball' : parsebasketball,
}

### don't even try to understand it ###
def printPretty(results, args):
	length = int(math.log(len(results), 10)) + 1
	in_length = max(length, len("In-Degree"))

	rank_length = int(math.log(args.epsilon, 10)) * -1
	rank_head_length = rank_length + 2

	length = str(length)
	in_length = str(in_length)
	rank_length = str(rank_length)
	rank_head_length = str(rank_head_length)

	body = "{0:>" + length + "}  {1:^30}  {2:." + rank_length + "f}  {3:>"+ in_length + "}"
	head = "{0:^" + length + "}  {1:^30}  {2:^" + rank_head_length + "}  {3:^" + in_length + "}"
	
	printResults(head, body, results)


###
#	Print results as CSV
###
def printReport(results, args):
	report = "{0},{1},{2},{3}"
	printResults(report, report, results)

def printResults(header, body, results):
	print header.format("", "ID", "Rank", "In-Degree")
	for ndx, node in enumerate(results):
		print body.format(ndx + 1, node, node.newRank, len(node.ins))

printers = {
	'table' : printPretty,
	'csv' : printReport,
}

def parse_and_rank(args):
	global parsers, printers

	graph = Graph()
	parse = parsers[args.type]

	parse_details = timeme(parse)(args.filename, graph)

	parse_time = parse_details[0]

	rank_time, results = pageRank(args.epsilon, args.clickProb, graph)

	ranking, iterations = results

	print "Parse/Read Time:", parse_time, "seconds"
	print "Iterations:", iterations
	print "Page Rank Time:", rank_time, "seconds"
	print "Items:"

	printers[args.printAs](ranking, args)


parser = argparse.ArgumentParser(description='Parse and Page Rank Graph')

parser.add_argument('filename', help='File containing graph edges')
parser.add_argument('--type', help='Type of parser to use for file', default='four', choices=['four', 'football', 'snap', 'bball'])
parser.add_argument('--epsilon', help='Error bound to determine when to stop ranking', default=math.pow(10, -7), type=float)
parser.add_argument('--clickProb', help='Probability that an edge will be followed when ranking', default=0.85, type=float)
parser.add_argument('--printAs', help='How to print results', default='csv', choices=['table', 'csv'])

args = parser.parse_args()

parse_and_rank(args)