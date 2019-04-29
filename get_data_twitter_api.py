from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results
import datetime
from math import floor
import pickle
import os
import time


def retrieve_twitter_data(query, begin_date, end_date, window_size, yaml_file_name, save_dir):
	"""
	simple function to retrieve data using the twitter premium API
	on a periodical basis with a user defined window size
	
	query: the query, see twitter premium search operators
	begin_date & end_date: begin and end dates (including)
	window_size: the size of the sliding window (size of the unit subperiod)
	yaml_file_name: full directory to the yaml file where twitter credentials are stored
	save_dir: directory where the data should be saved
	"""

	# setting the authenication methods
	premium_search_data = load_credentials(filename="~/.twitter_keys.yaml",
											yaml_key = 'search_tweets_api_data',
											env_overwrite = False)

	# converting dates to datetime format
	begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
	end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

	# determining the total number of days
	num_days = (end_date - begin_date).days + 1

	# determinig the total number of periods
	if num_days % window_size == 0:
		num_periods = int(num_days / window_size)
	else:
		num_periods = int(floor(num_days / window_size) + 1)

	# loop over the entire period
	for i in range(num_periods):
		# setting the from and end date vars (as defined by twitter premium operators)
		from_date = begin_date + datetime.timedelta(days = i * window_size)
		to_date = from_date + datetime.timedelta(days = window_size - 1)

		# convert back to str format as required by twitter api
		from_date = str(from_date)[:10]
		to_date = str(to_date)[:10]

		# setting the rule
		rule = gen_rule_payload(query,
								from_date = from_date,
								to_date = to_date,
								results_per_call=500)

		print('retrieving data ...')

		# get the data
		data = collect_results(rule, max_results = 500, result_stream_args = premium_search_data)

		print('data retrieved, there are', len(data), 'tweets')

		# save
		with open(os.path.join(save_dir, "_".join([from_date, to_date, '.pickle'])), 'wb') as handle:
			pickle.dump(data, handle)

		print('data saved, we are at iteration', i+1, 'of', num_periods, 'total iterations')
		time.sleep(1)



if __name__ == "__main__":
	query = input("please enter your query: ")
	begin_date = input("please enter begin date: ")
	end_date = input("please enter end date: ")
	window_size = input("please enter window size: ")
	window_size = int(window_size)
	yaml_file_name = input("please enter full yaml file directory: ")
	save_dir = input("please enter the save directory")
	print('now beginning to access Twitter premium search API ...')
	retrieve_twitter_data(query, begin_date, end_date, window_size, yaml_file_name, save_dir)
