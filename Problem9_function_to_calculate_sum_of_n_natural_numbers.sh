
# Problem 9
#
# Title: function_to_calculate_sum_of_n_natural_numbers

#
# Question: Write a function to get number n as an argument   
# 			and calculate this arithmentic series
#			1 + 2 + 3 + 4 + 5 + 6 + ... + n
#
# Example:  input: 6 ------------ output: 21


def calculate_sum(n):
	return sum(list(range(1,n+1)))
