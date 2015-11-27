# -*- encoding: utf-8 -*-
'It \'s a class'

__author__ = 'Todd Tse'



class student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
		
	def print_score(self):
		print('%s: %s' %(self.name,self.score))