
# Problem 10
#
# Title: count_trailing_zeroes
#
# Question: Ask for an input from user and count and 
#			display number of trailing zeros 
#
# Example:  input: 6000 ------------ output: 3

try:
	print(len([digit for digit in list(map(int,input(
	"Enter a number: ").strip())) if digit==0 ]))
	
except ValueError:
	print("Input Type Error")







