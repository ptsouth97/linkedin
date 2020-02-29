# LinkedIn Analyzer

## Overview
This application's purpose is to analyze the conversion rate of LinkedIn connections to involvement in a promotional drive

* User must download [LinkedIn](https://www.linkedin.com) connections data as well as [Udemy](https://www.udemy.com) student data
	1. Learn how to download LinkedIn data [here](https://www.linkedin.com/help/linkedin/answer/50191/accessing-your-account-data?lang=en)
* The application reads these files and converts to dataframes
* Next, a list provided by the user details the dates of the promotional drives
* The app filters both the connections and student dataframes using these dates
* Then the number of connections and students is counted
* These numbers are used to calculate the conversion rate
* Finally, this data is graphed

This application uses:
* [Pandas](https://pandas.pydata.org/)
