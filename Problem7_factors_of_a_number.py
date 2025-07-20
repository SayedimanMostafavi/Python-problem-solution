
# Problem 7
#
# Title: Factors_of_a_number
#
# Question: Ask for a number and print its factors as a list 
# 
# Example: input:12 -------- output:[1,2,3,4,6]

user_input = int(input("Enter a number: ").strip())
print([num for  num  in  range(1,user_input+1)  if  user_input % num == 0])
