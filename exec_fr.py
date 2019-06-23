from get_data_twitter_api import retrieve_twitter_data

# set var values
query = "intelligence artificielle OR IA profile_country: FR"
begin_date = "2016-04-18"
end_date = "2019-04-17"
window_size = 11
yaml_file_name = "~/.twitter_keys.yaml"
save_dir = "../master_thesis_data/twitter/FR"

retrieve_twitter_data(query, begin_date, end_date, window_size, yaml_file_name, save_dir)
