
# Problem 8
#
# Title: Recursive_function_to_reverse_string
#
# Question: Write a recursive function that get an string 
# 			as an argument and return reverse of it
#
# Example: input: Hello -------- output: olleH


def reverse_string(word):
	if len(word) <= 1 :
		return word
	return reverse_string(word[1:]) +  word[0]
	
