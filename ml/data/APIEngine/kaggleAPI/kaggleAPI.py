# import external libraries
from kaggle.api.kaggle_api_extended import KaggleApi

# constants
PATH = '../../datasets/'
KAGGLE_PATH = 'grouplens/movielens-20m-dataset'

# file names
file_names = ['link.csv', 'genome_tags.csv']

# keys authetication
api = KaggleApi()
api.authenticate()

# download singular file
[api.dataset_download_file(dataset=KAGGLE_PATH, file_name=i, path=PATH) for i in file_names]