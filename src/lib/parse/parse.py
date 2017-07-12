#parses NCAA_Football file, SNAP files, and
#other format files

import csv
import graph
import re

#This function parses csv files of states, karate,
#dolphin, and les miserables with repeated edges
def parsefour(filecsv, graph):
	with open(filecsv) as csvfile:
		reader = csv.reader(csvfile, delimiter = ',', quotechar = '"', skipinitialspace=True) 
		for row in reader:
			graph.addEdge(row[2], row[0])

#This function parses csv file NCAA_Football
#and checks values to ensure correct references
def parsefootball(filecsv, graph):
	with open(filecsv) as csvfile:
		reader = csv.reader(csvfile, delimiter = ',', quotechar = '"', skipinitialspace=True) 
		parse = ((row[0], int(row[1]), row[2], int(row[3])) for row in reader)
		for row in parse:
			if row[1] > row[3]:
				graph.addEdge(row[2], row[0])
			else:
				graph.addEdge(row[0], row[2])


#Parse snap file
def parseSNAP(filename, graph):
	with open(filename) as f:
		skipComments = (line for line in f if line[0] != '#')
		edges = (re.split("\s+", edge) for edge in skipComments)
		for edge in edges:
			graph.addEdge(edge[0], edge[1])

#This function parses csv file NCAA_Football
#and checks values to ensure correct references
def parsebasketball(filecsv, graph):
	with open(filecsv, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',', quotechar = '"', skipinitialspace=True) 
		parse = ((row[0], int(row[1]), row[2], int(row[3])) for row in reader)
		for row in parse:
			print row[0], row[2]
			if row[1] > row[3]:
				graph.addEdge(row[2], row[0])
			else:
				graph.addEdge(row[0], row[2])