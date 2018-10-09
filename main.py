#To Do
# -link array to sections
# -figure out sorting

import csv
import pandas

input_list=[]

print(f'1:incident_id\n2:case_number\n3:incident_datetime\n4:incident_type_primary\n5:incident_description\n6:clearance_type\n7:address_1\n8:address_2\n9:city\n10:state\n11:zip\n12:country\n14:latitude\n15:longitude\n16:created_at\n17:updated_at\n18:location\n19:hour_of_day\nday_of_week\n20:parent_incident_type\n')

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

print(f'Printing list...')
print(*input_list)

sortInput = int(input(f'Select the column you would like to sort by.\n'))
if not sortInput in input_list:
	print (f'Not in list.')
elif sortInput in input_list:
	print (f"In list. Sorting by",sortInput)

# out = pandas.read_csv('Riverside_County_Sheriff_Department.csv')



