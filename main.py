import csv
import pandas

#BUGS TO FIX:
# -entering anything besides an int will crash the loop
# -repeats are not working
# -you can only exit the loop by entering something out of range

input_list=[]

while 1:#userInput >= 1 and userInput <= 20:
	try:
		userInput = int(input("Please specify desired columns.\n"))
	except ValueError:
		print("Input must be of int type. Ending input loop.")
		break	
	if userInput < 1 or userInput > 20:
		print (f'Out of range.\n')
		continue
	elif userInput in input_list:
		print (f'You already entered this column value. Try another.')
		continue
	elif len(input_list) > 20:
		print (f'List is full. Ending input loop.')
		break
	else:
		input_list.append(userInput)

print(f"Printing list...\n")
print(*input_list, sep='\n')
print(f"Success")

