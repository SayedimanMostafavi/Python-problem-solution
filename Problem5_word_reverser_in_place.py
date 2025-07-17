
# Problem Number 5
#
# Title: Word Reverser In Place
# 
# Question: Ask for a sentence from user 
#                 and reverse each word in its place 
#     
# Example: Input: "Hello World" ------------ Ouput: "olleH dlroW"


try :
	print(" ".join(map(lambda x: x[ : : -1],input("Enter a sentence: ").strip().split())))

except ValueError:
	print("Input Type Error")
