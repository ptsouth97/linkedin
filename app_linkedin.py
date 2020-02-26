#!/usr/bin/python3

import pandas as pd

def main():
	''' Main function for testing'''

	file_name = "Connections.csv"

	dataframe = pd.read_csv(file_name)

	# print(dataframe.head)

	count_bcbas(dataframe)


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
