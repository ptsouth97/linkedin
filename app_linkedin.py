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

	# Read and convert Udemy Students csv to dataframe
	students_file_name = 'Students.csv'
	students = pd.read_csv(students_file_name)
	enrolled_date = 'Enrolled'

	# count_bcbas(dataframe)

	# Get dataframe for Udemy students who enrolled in course during a specific time range
	students = filter_dates(students, enrolled_date)

	# Split 'Student Name' column into 'FirstName' and 'LastName'
	students['Student Name'] = students['Student Name'].str.split(" ", n=1, expand=True)
	print(students.head)

	# Get LinkedIn connections who connected during that same time range
	connections = filter_dates(connections, connections_date)
	print(connections.head)

	# Merge Udemy Students and LinkedIn Connections based on name
	merged = connections.merge(students, left_on='FirstName', right_on='Student Name')
	print(merged.head)


def filter_dates(df, date_column):
	''' Filters dataframes based on date range'''

	start_date = '2019-12-05 00:00:00.000000'
	end_date = '2019-12-08 09:00:00.000000'

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


def promo_drive_1(df):
	''' calculates statistics for promotional drive 1'''

	start_date = '12/05/2019'
	end_date = '12/08/2019'

	course_name = 'Make Your Own Celeration Chart'

	return


if __name__ == '__main__':
	main()
