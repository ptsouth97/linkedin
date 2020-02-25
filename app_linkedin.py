#!/usr/bin/python3

import pandas as pd

def main():
	''' Main function for testing'''

	file_name = "Connections.csv"

	df = pd.read_csv(file_name)

	print(df.head)


if __name__ == '__main__':
	main()
