
# Problem Number 3
#
# Title: Average of Odd Digits
#
# Question: Ask for an integer from user and calculate average
#                  of its odd digits
# Example: Input: 376 ------------ Ouput: 5

from statistics import mean

try:
	print(f"Mean of odd digits if exist: {mean([ int(digit) for digit in list(
	map(int,input("Enter a positive integer: ").strip())) if digit%2 !=0 ])}")
	
except Exception:
	print("Input Type Error, Input only a positive integer")
