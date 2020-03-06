#!/usr/bin/python3

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


def main():
	''' Main function for testing'''
	
	# perform_analysis()

	# regression testing
	results = pd.read_csv('results.csv', index_col=0)
	regression(results)
	

def perform_analysis():
	''' Main loop for performing analysis'''

	# Read and convert LinkedIn Connections csv to dataframe
	connections_file_name = 'Connections.csv'
	connections = pd.read_csv(connections_file_name)
	connections_date = 'Connected On'
	
	# Change 'Connected On' column to date time format
	connections['Connected On'] = connections['Connected On'].apply(lambda x: dt.datetime.strptime(x, '%d %b %Y'))

	# Read and convert Udemy students csv from all classes to dataframe
	students = make_classes_df()
	enrolled_date = 'Enrolled'

	# Make a list of the promotion dates
	promotions = make_promos_list()

	# Get the first element in each list of promotion start/end dates
	promo_dates = [x[0] for x in promotions]

	# Convert promo date strings to datetime values
	# promo_dates = [dt.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in promo_dates]

	# Initialize a blank results dataframe
	columns=['Connections', 'Students', 'Conversion', 'Course']
	results = pd.DataFrame(index=promo_dates, columns=columns)
	
	for promo in promotions:

		# Get dataframe for Udemy students who enrolled in course during a specific time range
		promo_students = filter_dates(students, enrolled_date, promo)
		num_students = len(promo_students)
		results.loc[promo[0], 'Students'] = num_students

		# Add the course name
		results.loc[promo[0], 'Course'] = promo[2]

		# Get LinkedIn connections who connected during that same time range
		promo_connections = filter_dates(connections, connections_date, promo)
		num_connections = len(promo_connections)
		results.loc[promo[0], 'Connections'] = num_connections

		# Calculate the connections to enrollments converstion rate
		conversion_rate = num_students / num_connections * 100
		results.loc[promo[0], 'Conversion'] = conversion_rate

	print(results)
	print(type(results.index.values))
	results.to_csv('results.csv')

	for column in columns:

		make_graph(results, column, promo_dates)

	# End of application
	print('Good bye...')


def regression(df):
	''' performs linear regression on the results df'''

	print(df)
	X = df.index.values
	X = [dt.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in X]
	X = np.asarray([(x - X[0]).days for x in X]).reshape(-1, 1)
	#X = [dt.datetime.days(x) for x in X]

	y = df['Conversion']
	print(X)
	print(type(X[0]))
	# Create the regressor: reg
	reg = LinearRegression()

	# Create the prediction space
	prediction_space = np.linspace(min(X), max(X)).reshape(-1,1)

	# Fit the model to the data
	reg.fit(X, y)

	# Compute predictions over the prediction space: y_pred
	y_pred = reg.predict(prediction_space)

	# Plot regression line
	plt.plot(prediction_space, y_pred, color='black', linewidth=3)
	plt.show()

	return


def make_graph(df, col, dates):
	''' displays graph of results'''

	# Split the string datetimes at the space
	dates = [ date.split() for date in dates ]
	dates = [ date[0] for date in dates ]

	# Slice the appropriate column
	df = df[col]
	
	# Make the plot	
	df.plot(linestyle='none', marker='o')
	plt.title('LinkedIn Promotion')
	plt.xlabel('start date of promotion')
	plt.ylabel(col)
	plt.xticks(np.arange(len(df)), dates, rotation=45)
	plt.show()		

	return


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
	
	# list [promo start date, promo end date, course title]
	promotions = [['2019-12-05 09:00:00', '2019-12-08 09:00:00', 'celeration'], \
                  ['2019-12-08 16:00:00', '2019-12-11 16:00:00', 'drive'], \
                  ['2020-01-23 11:00:00', '2020-01-26 11:00:00', 'drive'], \
                  ['2020-02-03 11:00:00', '2020-02-06 11:00:00', 'celeration'], \
                  ['2020-02-10 11:00:00', '2020-02-13 11:00:00', 'wearables'], \
                  ['2020-02-18 11:00:00', '2020-02-21 11:00:00', 'drive']]

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
