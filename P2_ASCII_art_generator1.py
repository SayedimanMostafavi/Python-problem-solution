
#  Problem number 2
#
#  Title: ASCII Art Generator 1
#  
#  Question: Ask for the number of rows from user and write a 
# 				    Python code to generate this pattern  
# 
#  Example Output: input: 4 ----------- output: 
#											                            * - * - * -
#      									                            * - * - * -
#     										                            * - * - * -
#     										                            * - * - * -

try:
	print("\n".join(["* - * - * - "]*abs(int(input("Enter the number of rows: ").strip()))))
		
		
except ValueError:
	print("Input Type Error !!!")
	

"""	

# Solution 2 (Nested Loop) (Classical Aproach)

try:
	number_of_rows = int(input("Enter the number of rows: ").strip()) # Get the number of rows from user
	for row in range(number_of_rows):       					      # First for-loop handles the rows 
		for column in range(3):                						      # Second for-loop handles the columns 
			print("* -",end=" ")               						          # Printing pattern for each two-column (* -)
		print()		            													  # without going to next line 
																			  
			
except ValueError:
	print("Input Type Error")

"""
