
# Problem Number 4
#
# Title: Middle Digit
#
# Question: Ask for an integer from user and display the middle digit 
#                 (if the number of digits is even return the average of two 
#                 middle digit)
# Example: Input: 376 ------------ Ouput: 7
# Example: Input: 3456 ---------- Output: 4.5

try:
	ui = list(map(int,input("Enter a positive integer: ").strip()))
	print( ui[len(ui)//2]  if  len(ui)%2 != 0  else  (ui[len(ui)//2-1]+ui[len(ui)//2])/2 ) 

except Exception:
		print("Wrong input")
