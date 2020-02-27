#!/usr/bin/python3

import pandas as pd
import datetime as dt


def main():
	''' Main function for testing'''
	
	# Read and convert LinkedIn Connections csv to dataframe
	connections_file_name = 'Connections.csv'
	connections = pd.read_csv(connections_file_name)
	connections_date = 'Connected On'
	
	# Change 'Connected On' column to date time
	connections['Connected On'] = connections['Connected On'].apply(lambda x: dt.datetime.strptime(x, '%d %b %Y'))

	# Read and convert Udemy students csv from all classes to dataframe
	students = make_classes_df()
	enrolled_date = 'Enrolled'

	# Make a list of the promotion dates
	promotions = make_promos_list()

	# Get the first element in each list of promotion start/end dates
	promo_dates = [x[0] for x in promotions]

	# Initialize a blank results dataframe
	results = pd.DataFrame(index=promo_dates, columns=['Connections', 'Students', 'Conversion'])
	
	for promo in promotions:

		# Get dataframe for Udemy students who enrolled in course during a specific time range
		promo_students = filter_dates(students, enrolled_date, promo)
		num_students = len(promo_students)
		results.loc[promo[0], 'Students'] = num_students

		# Get LinkedIn connections who connected during that same time range
		promo_connections = filter_dates(connections, connections_date, promo)
		num_connections = len(promo_connections)
		results.loc[promo[0], 'Connections'] = num_connections

		# Merge Udemy Students and LinkedIn Connections based on name
		# merged = connections.merge(students, left_on='FirstName', right_on='Student Name')
		#print(merged.head)

		# Calculate the connections to enrollments converstion rate
		conversion_rate = num_students / num_connections * 100
		results.loc[promo[0], 'Conversion'] = conversion_rate

		# Display conversion rate
		print('During the promotion on dates {} to {}:'.format(promo[0], promo[1]))
		print('{} connections were made on LinkedIn'.format(str(num_connections)))
		print('{} students enrolled on Udemy'.format(str(num_students)))
		print('For a connection to enrollment conversion rate of {:.2f}'.format(conversion_rate))
		print('')

	print(results)


def make_classes_df():
	''' reads each Udemy class .csv and appends them to dataframe'''

	# List containing names of the csv files containing Udemy student info
	classes = ['google_drive.csv', 'celeration.csv', 'wearables.csv']
	
	# Initialize empty dataframe
	master = pd.DataFrame()

	for a_class in classes:

		# Read the current class's csv and convert to a dataframe
		students = pd.read_csv(a_class)
		
		# Split 'Student Name' column into 'FirstName' and 'LastName'
		students['Student Name'] = students['Student Name'].str.split(" ", n=1, expand=True)

		master = master.append(students)

	master = master.reset_index(drop=True)

	return master
		

def make_promos_list():
	'''  Make a list of promotions dates'''
	
	promotions = [['2019-12-05 09:00:00.000000', '2019-12-08 09:00:00.000000'], \
                  ['2019-12-08 16:00:00.000000', '2019-12-11 16:00:00.000000'], \
                  ['2020-01-23 11:00:00.000000', '2020-01-26 11:00:00.000000'], \
                  ['2020-02-03 11:00:00.000000', '2020-02-06 11:00:00.000000'], \
                  ['2020-02-10 11:00:00.000000', '2020-02-13 11:00:00.000000'], \
                  ['2020-02-18 11:00:00.000000', '2020-02-21 11:00:00.000000']]

	return promotions


def filter_dates(df, date_column, dates):
	''' Filters dataframes based on date range'''

	start_date = dates[0]
	end_date = dates[1]

	filtered_1 = df.loc[df[date_column] >= start_date]
	filtered = filtered_1.loc[filtered_1[date_column] <= end_date]

	return filtered


def count_bcbas(df):
	''' counts the number of BCBAs and BCaBAs in the dataset'''

	# print(list(df.columns.values))
	total = len(df)
	print(total)

	# Create a list of keywords relevant to BCBA positions
	searchfor = ['BCBA', \
                 'Bcba', \
                 'bcba', \
                 'Behavior Analyst', \
                 'behavior analyst', \
                 'Behavior Consultant', \
                 'Clinical Supervisor', \
                 'Clinical Manager', \
                 'Clinical Director', \
                 'Supervising', \
                 'Board Certified Behavior Analyst' \
                 'LBA', \
                 'B.C.B.A', \
                 'Clinician', \
                 'ABA Training Coordinator']

	# Slice rows with positions contains key words in the 'searchfor' list
	bcba_position =df[ df['Position'].str.contains('|'.join(searchfor), na=False)]
	
	print(bcba_position)

	print(len(bcba_position))

	return


if __name__ == '__main__':
	main()
