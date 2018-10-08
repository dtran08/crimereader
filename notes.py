#reads the file by printing each row plus its data and returning the number of lines processed
# with open('Riverside_County_Sheriff_Department.csv') as csv_file:
# 	csv_reader = csv.reader(csv_file, delimiter=',')
# 	line_count = 0
# 	for row in csv_reader:
# 		if line_count == 0:
# 			print(f'Column names are {", ".join(row)}')
# 			line_count +=1
# 		else:
# 			print(f'\t{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]} {row[11]} {row[12]} {row[13]} {row[14]} {row[15]} {row[16]} {row[17]} {row[18]} {row[19]}')
# 			line_count += 1
# 	print(f'Processed {line_count} lines.')



#reads the file into a dictionary, or list/array
# with open('Riverside_County_Sheriff_Department.csv', mode='r') as csv_file:
# 	csv_reader = csv.DictReader(csv_file)
# 	line_count = 0
# 	for row in csv_reader:
# 		if line_count == 0:
# 			print(f'Column names are {", ".join(row)}')
# 			line_count += 1
# 		print(f'\t{row["incident_id"]} and {row["case_number"]}')
# 		line_count += 1
# 	print(f'Processed {line_count} lines.')



#write to a NEW csv file
# with open('crime_file.csv', mode='w') as crime_file:
# 	crime_writer = csv.writer(crime_file, delimiter=',', quotechar='"',)

# 	crime_writer.writerow(['asdf', 'ghjk', 'qwerty'])
# 	crime_writer.writerow(['153', '170', '161', '135'])



#write to a new csv file from a dictionary
# with open('crime_file.csv', mode='w') as crime_file:
# 	fieldnames= ['incident_id', 'case_number', 'incident_datetime']
# 	writer = csv.DictWriter(crime_file, fieldnames=fieldnames)

# 	writer.writeheader()
# 	writer.writerow({'incident_id': 'ID1', 'case_number': 'CN1', 'incident_datetime': 'IDT1'})
# 	writer.writerow({'incident_id': 'ID2', 'case_number': 'CN2', 'incident_datetime': 'IDT2'})
# 	writer.writerow({'incident_id': 'ID3', 'case_number': 'CN3', 'incident_datetime': 'IDT3'})


# Reads info to dataframe (compressed for larger files)
# df = pandas.read_csv('Riverside_County_Sheriff_Department.csv')
# print(df)
#will go over dataframes later, for now we're focusing on outputting it in a certain way to csv



# read/print starting from the index_col column
# df = pandas.read_csv('Riverside_County_Sheriff_Department.csv', index_col='case_number')
# print(df)

# formats to organize by index_col
# df = pandas.read_csv('Riverside_County_Sheriff_Department.csv', index_col='parent_incident_type', parse_dates=['day_of_week'])
# df.to_csv('output.csv')


# df = pandas.read_csv('Riverside_County_Sheriff_Department.csv',
# 			index_col='incident_id',
# 			parse_dates=['case_number'],
# 			header=0,
# 			names=['incident_id', 'case_number', 'incident_datetime',
# 			'incident_type_primary', 'incident_description',
# 			'clearance_type', 'address_1', 'address_2', 'city',
# 			'state', 'zip', 'country', 'latitude', 'longitude',
# 			'created_at', 'location', 'hour_of_day', 'day_of_week',
# 			'parent_incident_type'])
# df.to_csv('output.csv')
# print(df)