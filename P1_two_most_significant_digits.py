
#  Problem Number 1 
# 
#  Title: Two Most Significant Digits (Two Leftmost Digits)
# 
#  Question: Ask for an integer from user and diplay the two most significant digits 
#                  (the two leftmost digits) and the number if it is less than 10  
# 
#  Exaple Output: input: -345 ----------output: 34


try: 
	print(f"The most two significant digits: {str(abs(int(input(
	"Enter an integer: ").strip())))[:2]}")

except ValueError:
	print("Type Error: Retry!")





"""

#  Solution 1 (Expanded version)

try:
	user_input = input("Enter an integer: ").strip()  # Get user input and remove the leading and trailing apaces
	user_input = int(user_input) 		                       # Cast user input to integer , using int() function
	user_input = abs(user_input)                           # use abs() function (absolute value) to handle negative input
	user_input = str(user_input)                             # use str() function to convert it to string agian to access 
																			  # first and second digits using slicing[0:2]  
	print("Two most significant digits: ", user_input[0:2])  #In python strings are considered as an array of characters  
																			  #so we can use 0-base index to access the items
 
except ValueError:
	print("Type Error: Retry!")

"""
