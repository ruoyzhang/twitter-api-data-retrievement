from get_data_twitter_api import retrieve_twitter_data

# set var values
query = "artificial intelligence OR AI OR IA OR intelligence artificielle profile_country: BE"
begin_date = "2016-04-17"
end_date = "2019-04-17"
window_size = 11
yaml_file_name = "~/.twitter_keys.yaml"
save_dir = "../master_thesis_data/twitter/BE"

retrieve_twitter_data(query, begin_date, end_date, window_size, yaml_file_name, save_dir)