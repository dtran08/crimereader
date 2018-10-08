import csv
import pandas

#BUGS TO FIX:
-entering anything besides an int will crash the loop
-repeats are not working
-you can only exit the loop by entering something out of range

input_list=[]

userInput = int(input("Please specify desired columns.\n"))

while userInput >= 1 and userInput <= 20:
	userInput = int(input("Please specify desired columns.\n"))
	if userInput in input_list:
		print (f'You already entered this column value. Try another or press the ; key to exit.')
	else:
		input_list.append(userInput)


print(f"Success")

