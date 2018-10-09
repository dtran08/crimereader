#To Do
#-ONLY sort by what columns the user specifies

import csv
import pandas
import os.path
from os import path

input_list=[]

print(f'1:incident_id\n2:case_number\n3:incident_datetime\n4:incident_type_primary\n5:incident_description\n6:clearance_type\n7:address_1\n8:address_2\n9:city\n10:state\n11:zip\n12:country\n13:latitude\n14:longitude\n15:created_at\n16:updated_at\n17:location\n18:hour_of_day\n19:day_of_week\n20:parent_incident_type\n')

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
	if sortInput == 1:
		print (f"In list. Sorting by incident_id",sortInput)
	if sortInput == 2:
		print (f"In list. Sorting by case_number",sortInput)
	if sortInput == 3:
		print (f"In list. Sorting by incident_datetime",sortInput)
	if sortInput == 4:
		print (f"In list. Sorting by incident_type_primary",sortInput)
	if sortInput == 5:
		print (f"In list. Sorting by incident_description",sortInput)
	if sortInput == 6:
		print (f"In list. Sorting by clearance_type",sortInput)
	if sortInput == 7:
		print (f"In list. Sorting by address_1",sortInput)
	if sortInput == 8:
		print (f"In list. Sorting by address_2",sortInput)
	if sortInput == 9:
		print (f"In list. Sorting by city",sortInput)
	if sortInput == 10:
		print (f"In list. Sorting by state",sortInput)
	if sortInput == 11:
		print (f"In list. Sorting by zip",sortInput)
	if sortInput == 12:
		print (f"In list. Sorting by country",sortInput)
	if sortInput == 13:
		print (f"In list. Sorting by latitude",sortInput)
	if sortInput == 14:
		print (f"In list. Sorting by longitude",sortInput)
	if sortInput == 15:
		print (f"In list. Sorting by created_at",sortInput)
	if sortInput == 16:
		print (f"In list. Sorting by updated_at",sortInput)
	if sortInput == 17:
		print (f"In list. Sorting by location",sortInput)
	if sortInput == 18:
		print (f"In list. Sorting by hour_of_day",sortInput)
	if sortInput == 19:
		print (f"In list. Sorting by day_of_week",sortInput)
	if sortInput == 20:
		print (f"In list. Sorting by parent_incident_type",sortInput)

# out = pandas.read_csv('Riverside_County_Sheriff_Department.csv')

incident_id = 1
case_number = 2
incident_datetime = 3
incident_type_primary = 4
incident_description = 5
clearance_type = 6
address_1 = 7
address_2 = 8
city = 9
state = 10
zip = 11
country = 12
latitude = 13
longitude = 14
created_at = 15
updated_at = 16
location = 17
hour_of_day = 18
day_of_week = 19
parent_incident_type = 20

#super long brute force if statements
print (f"Creating csv file. One moment.")
print (f'.')
print (f'..')
print (f'...')
if sortInput == 1:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'incident_id')
elif sortInput == 2:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'case_number')	
elif sortInput == 3:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'incident_datetime')	
elif sortInput == 4:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'incident_type_primary')	
elif sortInput == 5:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'incident_description')	
elif sortInput == 6:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'clearance_type')	
elif sortInput == 7:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'address_1')	
elif sortInput == 8:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'address_2')	
elif sortInput == 9:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'city')	
elif sortInput == 10:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'state')	
elif sortInput == 11:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'zip')	
elif sortInput == 12:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'country')	
elif sortInput == 13:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'latitude')	
elif sortInput == 14:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'longitude')	
elif sortInput == 15:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'created_at')	
elif sortInput == 16:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'updated_at')	
elif sortInput == 17:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'location')	
elif sortInput == 18:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'hour_of_day')	
elif sortInput == 19:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'day_of_week')	
elif sortInput == 20:
	df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
	index_col = 'parent_incident_type')	
df.to_csv('final_output.csv')
if path.exists('final_output.csv'):
	print(f"File created successfully.")
else:
	print(f"Error, file not created.")
# if userInput == zip:
# 	print(f"SUCC")



