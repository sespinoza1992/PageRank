#!/usr/bin/python
import time
import weakref

class Tuple(tuple):
	pass


memos = {}

def clear_t(name):
	global memos
	memos[name].clear()

def memoize_t(name):
	global memos
	memos[name] = {}
	return lambda f: memoize(f, memos[name])


def memoize(func, memo = {}):
	def wrapper(*args):
		if args not in memo:
			memo[args] = func(*args)
		return memo[args]
	return wrapper

def timeme(func):
	def wrapper(*args):
		startTime = time.time()
		res = func(*args)
		endTime = time.time()
		return (endTime - startTime, res)
	return wrapper