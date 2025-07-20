
# Problem 6
#
# Title: Function_to_calculate_range_of_list
#
# Question: Write a function that take an integer list 
#           and return its range 
# 
# Explanation: Range = max - min + 1


def calculate_range(lst):
	return max(lst)-min(lst)+1  if  lst  else  0
	
