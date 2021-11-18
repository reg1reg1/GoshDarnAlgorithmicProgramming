'''
Given 2 jugs of capacity n,m
d < n
Figure out how to measure d in the shortest amount of steps
Approach : Using BFS is slow but intuitive
Faster approach by using maths and gcd
'''
import os
import sys
import collections
def solve2Jugs(m,n,d):
	Q = collections.deque()
	Q.append((0,0))
	while Q.empty() is False:
		tup = Q.popleft()





